"""LLM client wrapper supporting Groq + Google Gemini.

Key resolution order (per provider):
1. Env var (GROQ_API_KEY / GEMINI_API_KEY)
2. Streamlit session state
3. %APPDATA%/chat-coach-v2/.env (Windows-only, ignored when not present)
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Iterable

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = ["Gemini", "Groq"]

MODELS = {
    "Groq": ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
    "Gemini": ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-flash-lite"],
}

DEFAULT_PROVIDER = "Gemini"
DEFAULT_MODEL = "gemini-2.5-flash"
FALLBACK_MODEL = "llama-3.1-8b-instant"

KEY_ENV_BY_PROVIDER = {
    "Groq": "GROQ_API_KEY",
    "Gemini": "GEMINI_API_KEY",
}


def _user_config_path() -> Path | None:
    appdata = os.getenv("APPDATA")
    if not appdata:
        return None
    return Path(appdata) / "chat-coach-v2" / ".env"


def _load_from_user_config(key_name: str) -> str:
    path = _user_config_path()
    if not path or not path.is_file():
        return ""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            if k.strip() == key_name:
                return v.strip().strip('"').strip("'")
    except OSError:
        pass
    return ""


def resolve_key(provider: str) -> str:
    env = KEY_ENV_BY_PROVIDER.get(provider, "")
    if not env:
        return ""
    return (
        os.getenv(env)
        or st.session_state.get(f"{provider.lower()}_key", "")
        or _load_from_user_config(env)
    )


def _provider() -> str:
    return st.session_state.get("provider", DEFAULT_PROVIDER)


def _model() -> str:
    p = _provider()
    return st.session_state.get("model") or MODELS[p][0]


def _missing_key(provider: str) -> RuntimeError:
    env = KEY_ENV_BY_PROVIDER[provider]
    return RuntimeError(
        f"Missing {env}. Set it in the sidebar, a .env file, "
        f"or %APPDATA%/chat-coach-v2/.env."
    )


# ---------- Groq ----------

@st.cache_resource(show_spinner=False)
def _groq_client_cached(key: str):
    from groq import Groq
    return Groq(api_key=key)


def _groq_client():
    key = resolve_key("Groq")
    if not key:
        raise _missing_key("Groq")
    return _groq_client_cached(key)


def _groq_chat(messages, model, temperature, json_mode):
    kwargs = {"model": model, "messages": messages, "temperature": temperature}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    resp = _groq_client().chat.completions.create(**kwargs)
    return resp.choices[0].message.content or ""


def _groq_stream(messages, model, temperature):
    stream = _groq_client().chat.completions.create(
        model=model, messages=messages, temperature=temperature, stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ---------- Gemini ----------

@st.cache_resource(show_spinner=False)
def _gemini_client_cached(key: str):
    from google import genai
    return genai.Client(api_key=key)


def _gemini_client():
    key = resolve_key("Gemini")
    if not key:
        raise _missing_key("Gemini")
    return _gemini_client_cached(key)


def _gemini_convert(messages):
    """Split system prompt from messages and convert to Gemini Content format."""
    from google.genai import types
    sys_parts = []
    contents = []
    for m in messages:
        role = m["role"]
        text = m["content"]
        if role == "system":
            sys_parts.append(text)
            continue
        g_role = "user" if role == "user" else "model"
        contents.append(types.Content(
            role=g_role, parts=[types.Part.from_text(text=text)]
        ))
    system_instruction = "\n\n".join(sys_parts) if sys_parts else None
    return system_instruction, contents


def _gemini_config(temperature, json_mode, system_instruction):
    from google.genai import types
    kwargs = {"temperature": temperature}
    if system_instruction:
        kwargs["system_instruction"] = system_instruction
    if json_mode:
        kwargs["response_mime_type"] = "application/json"
    return types.GenerateContentConfig(**kwargs)


def _gemini_chat(messages, model, temperature, json_mode):
    sys_inst, contents = _gemini_convert(messages)
    cfg = _gemini_config(temperature, json_mode, sys_inst)
    return _gemini_call_with_retry(model, contents, cfg)


def _gemini_call_with_retry(model, contents, cfg, *, max_attempts: int = 4):
    """Retry on 503/UNAVAILABLE / 429 with exponential backoff, then
    auto-fallback from gemini-2.5-pro to gemini-2.5-flash."""
    fallback_chain = [model]
    if model == "gemini-2.5-pro":
        fallback_chain.append("gemini-2.5-flash")
    elif model == "gemini-2.5-flash":
        fallback_chain.append("gemini-2.5-flash-lite")

    last_err: Exception | None = None
    for m in fallback_chain:
        for attempt in range(max_attempts):
            try:
                resp = _gemini_client().models.generate_content(
                    model=m, contents=contents, config=cfg,
                )
                return resp.text or ""
            except Exception as e:
                msg = str(e)
                last_err = e
                transient = ("503" in msg or "UNAVAILABLE" in msg
                             or "429" in msg or "RESOURCE_EXHAUSTED" in msg
                             or "overloaded" in msg.lower())
                if not transient:
                    raise
                if attempt < max_attempts - 1:
                    time.sleep(2 ** attempt)  # 1s, 2s, 4s
        # exhausted retries for this model — try the next fallback
    raise last_err if last_err else RuntimeError("Gemini call failed")


def _gemini_stream(messages, model, temperature):
    sys_inst, contents = _gemini_convert(messages)
    cfg = _gemini_config(temperature, False, sys_inst)
    fallback_chain = [model]
    if model == "gemini-2.5-pro":
        fallback_chain.append("gemini-2.5-flash")
    elif model == "gemini-2.5-flash":
        fallback_chain.append("gemini-2.5-flash-lite")
    last_err: Exception | None = None
    for m in fallback_chain:
        try:
            stream = _gemini_client().models.generate_content_stream(
                model=m, contents=contents, config=cfg,
            )
            for chunk in stream:
                if chunk.text:
                    yield chunk.text
            return
        except Exception as e:
            msg = str(e)
            last_err = e
            transient = ("503" in msg or "UNAVAILABLE" in msg
                         or "429" in msg or "overloaded" in msg.lower())
            if not transient:
                raise
    if last_err:
        raise last_err


# ---------- Public API ----------

def chat(messages: list[dict], *, model: str | None = None,
         temperature: float = 0.4, json_mode: bool = False) -> str:
    p = _provider()
    m = model or _model()
    if p == "Groq":
        return _groq_chat(messages, m, temperature, json_mode)
    return _gemini_chat(messages, m, temperature, json_mode)


def stream_chat(messages: list[dict], *, model: str | None = None,
                temperature: float = 0.6) -> Iterable[str]:
    p = _provider()
    m = model or _model()
    if p == "Groq":
        return _groq_stream(messages, m, temperature)
    return _gemini_stream(messages, m, temperature)


def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end != -1:
            return json.loads(text[start : end + 1])
        raise
