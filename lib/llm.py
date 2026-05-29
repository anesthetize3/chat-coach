"""Groq LLM client wrapper.

Key resolution order (first hit wins):
1. Env var GROQ_API_KEY (used by Streamlit Cloud secrets, .env, shell)
2. Streamlit session state (sidebar input)
3. Local user config file at %APPDATA%/chat-coach-v2/.env  (Windows-only,
   ignored by the deployed app since that path doesn't exist there)
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"


def _user_config_path() -> Path | None:
    """Return %APPDATA%/chat-coach-v2/.env if APPDATA is set, else None."""
    appdata = os.getenv("APPDATA")
    if not appdata:
        return None
    return Path(appdata) / "chat-coach-v2" / ".env"


def _load_from_user_config() -> str:
    """Read GROQ_API_KEY from the user's AppData config. Silent on missing."""
    path = _user_config_path()
    if not path or not path.is_file():
        return ""
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            if k.strip() == "GROQ_API_KEY":
                return v.strip().strip('"').strip("'")
    except OSError:
        pass
    return ""


def _resolve_key() -> str:
    return (
        os.getenv("GROQ_API_KEY")
        or st.session_state.get("groq_key", "")
        or _load_from_user_config()
    )


def _client():
    from groq import Groq
    key = _resolve_key()
    if not key:
        raise RuntimeError(
            "Missing GROQ_API_KEY. Set it via the sidebar, a .env file, "
            "or %APPDATA%/chat-coach-v2/.env."
        )
    return Groq(api_key=key)


def chat(messages: list[dict], *, model: str | None = None,
         temperature: float = 0.4, json_mode: bool = False) -> str:
    client = _client()
    kwargs = {
        "model": model or st.session_state.get("model", DEFAULT_MODEL),
        "messages": messages,
        "temperature": temperature,
    }
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    resp = client.chat.completions.create(**kwargs)
    return resp.choices[0].message.content or ""


def stream_chat(messages: list[dict], *, model: str | None = None,
                temperature: float = 0.6) -> Iterable[str]:
    client = _client()
    stream = client.chat.completions.create(
        model=model or st.session_state.get("model", DEFAULT_MODEL),
        messages=messages,
        temperature=temperature,
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


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
