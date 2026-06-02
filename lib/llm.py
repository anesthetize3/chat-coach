"""LLM client wrapper supporting Groq + Google Gemini.

Key resolution order (per provider):
1. Env var (GROQ_API_KEY / GEMINI_API_KEY)
2. Streamlit session state
3. %APPDATA%/chat-coach-v2/.env (Windows-only, ignored when not present)
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Iterable

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = ["Gemini", "Groq"]

MODELS = {
    "Groq": [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "meta-llama/llama-4-scout-17b-16e-instruct",
        "meta-llama/llama-4-maverick-17b-128e-instruct",
    ],
    "Gemini": ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.5-flash-lite"],
}

GROQ_QUOTA_FALLBACK_MODEL = "llama-3.3-70b-versatile"

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

_RETRY_AFTER_RE = re.compile(
    r"try again in\s+(?:(\d+)h)?\s*(?:(\d+)m)?\s*(?:([\d.]+)s)?",
    re.IGNORECASE,
)


def _is_quota_error(e: Exception) -> bool:
    msg = str(e)
    return ("429" in msg or "RESOURCE_EXHAUSTED" in msg
            or "quota" in msg.lower() or "rate" in msg.lower())


def _parse_retry_after(msg: str) -> float | None:
    """Extract a cooldown (seconds) from a provider error message.
    Groq: 'Please try again in 4m39.936s'. Returns None if not present."""
    m = _RETRY_AFTER_RE.search(msg)
    if not m or not any(m.groups()):
        return None
    h = float(m.group(1) or 0)
    mi = float(m.group(2) or 0)
    s = float(m.group(3) or 0)
    total = h * 3600 + mi * 60 + s
    return total if total > 0 else None


def _notify_fallback(from_provider: str, from_model: str,
                     to_provider: str, to_model: str) -> None:
    same = from_provider == to_provider
    what = "model" if same else "provider"
    note = (f"⚠️ {from_provider} ({from_model}) hit its quota — "
            f"switched {what} to {to_provider} ({to_model}) for this call.")
    st.session_state["llm_fallback_notice"] = note
    try:
        st.toast(note, icon="⚠️")
    except Exception:
        pass


# ---------- Quota tracking (lazy, no probe) ----------
#
# We LEARN from real failures. When a chat() call raises a quota error we
# record an entry keyed by (provider, model) in
# `st.session_state["quota_exhausted"]`. Providers like Groq enforce per-model
# TPD limits, so other models in the same provider may still be usable —
# fallback tries those FIRST before crossing to the other provider.
#
# Cooldown is derived from the error message when possible (e.g. Groq's
# "Please try again in 4m39s"); otherwise we use a conservative default.

QUOTA_DEFAULT_COOLDOWN_SECONDS = 5 * 60
QUOTA_MAX_COOLDOWN_SECONDS = 24 * 3600  # cap so a typo can't lock for years


def _quota_map() -> dict:
    m = st.session_state.get("quota_exhausted")
    if not isinstance(m, dict):
        m = {}
        st.session_state["quota_exhausted"] = m
    return m


def _qkey(provider: str, model: str) -> str:
    return f"{provider}::{model}"


def mark_quota_exhausted(provider: str, model: str, reason: str = "") -> None:
    cooldown = _parse_retry_after(reason) or QUOTA_DEFAULT_COOLDOWN_SECONDS
    cooldown = min(cooldown, QUOTA_MAX_COOLDOWN_SECONDS)
    _quota_map()[_qkey(provider, model)] = {
        "at": time.time(),
        "cooldown": cooldown,
        "provider": provider,
        "model": model,
        "reason": reason[:200],
    }


def clear_quota(provider: str | None = None, model: str | None = None) -> None:
    m = _quota_map()
    if provider is None:
        m.clear()
        return
    for key in [k for k, v in m.items()
                if v.get("provider") == provider
                and (model is None or v.get("model") == model)]:
        m.pop(key, None)


def is_quota_exhausted(provider: str, model: str) -> bool:
    entry = _quota_map().get(_qkey(provider, model))
    if not entry:
        return False
    cooldown = float(entry.get("cooldown", QUOTA_DEFAULT_COOLDOWN_SECONDS))
    if time.time() - float(entry.get("at", 0)) > cooldown:
        _quota_map().pop(_qkey(provider, model), None)
        return False
    return True


def is_provider_fully_exhausted(provider: str) -> bool:
    """True only if every known model for this provider is exhausted."""
    return all(is_quota_exhausted(provider, m) for m in MODELS.get(provider, []))


def quota_status(provider: str, model: str) -> dict | None:
    entry = _quota_map().get(_qkey(provider, model))
    if not entry:
        return None
    cooldown = float(entry.get("cooldown", QUOTA_DEFAULT_COOLDOWN_SECONDS))
    elapsed = time.time() - float(entry.get("at", 0))
    left = cooldown - elapsed
    if left <= 0:
        _quota_map().pop(_qkey(provider, model), None)
        return None
    return {**entry, "seconds_left": int(left)}


def all_quota_statuses() -> list[dict]:
    """Snapshot of currently-active quota entries, for UI display."""
    out = []
    for prov, models in MODELS.items():
        for mdl in models:
            s = quota_status(prov, mdl)
            if s:
                out.append(s)
    return out


def _next_available_model(provider: str, after: str | None) -> str | None:
    """Return the next model in MODELS[provider] (after `after`, wrapping) that
    is not currently quota-exhausted. None if all are exhausted."""
    models = MODELS.get(provider, [])
    if not models:
        return None
    start = (models.index(after) + 1) if after in models else 0
    order = models[start:] + models[:start]
    for m in order:
        if not is_quota_exhausted(provider, m):
            return m
    return None


def _alt_provider(current: str) -> tuple[str, str] | None:
    """Pick the other provider + a non-exhausted model from it, if a key is
    configured. Returns None if no viable alternate exists."""
    alt = "Groq" if current == "Gemini" else "Gemini"
    if not resolve_key(alt):
        return None
    alt_model = _next_available_model(alt, None)
    if alt_model is None:
        return None
    return alt, alt_model


def ensure_quota_or_switch() -> str | None:
    """Pre-flight check before a chat session. No API call — purely consults
    the in-memory quota map populated by previous real failures.

    If the active (provider, model) is exhausted, switch to:
      1) another model in the same provider, if available; else
      2) a model in the other provider, if a key is configured.
    """
    provider = st.session_state.get("provider", DEFAULT_PROVIDER)
    model = st.session_state.get("model") or MODELS[provider][0]
    if not is_quota_exhausted(provider, model):
        return None

    # 1) Same-provider model swap
    next_model = _next_available_model(provider, model)
    if next_model:
        st.session_state["model"] = next_model
        notice = (f"⚠️ {provider} ({model}) is over its quota — switched "
                  f"model to {next_model} for this session.")
        st.session_state["llm_fallback_notice"] = notice
        try:
            st.toast(notice, icon="⚠️")
        except Exception:
            pass
        return notice

    # 2) Cross-provider swap
    alt = _alt_provider(provider)
    if alt is None:
        notice = (f"⚠️ All {provider} models are over quota and no alternate "
                  "provider is configured. Add the other provider's API key "
                  "to fall back.")
        st.session_state["llm_fallback_notice"] = notice
        return notice

    alt_p, alt_m = alt
    st.session_state["provider"] = alt_p
    st.session_state["model"] = alt_m
    notice = (f"⚠️ All {provider} models are over quota — switched provider "
              f"to {alt_p} ({alt_m}) for this session.")
    st.session_state["llm_fallback_notice"] = notice
    try:
        st.toast(notice, icon="⚠️")
    except Exception:
        pass
    return notice


def _fallback_chain(provider: str, model: str) -> list[tuple[str, str]]:
    """Build an ordered list of (provider, model) candidates to try:
    1. The requested (provider, model).
    2. All other models in the same provider (in MODELS order, skipping
       already-exhausted ones).
    3. All models of the other provider (if a key is configured), again
       skipping exhausted ones.
    """
    chain: list[tuple[str, str]] = [(provider, model)]
    for m in MODELS.get(provider, []):
        if m == model:
            continue
        if not is_quota_exhausted(provider, m):
            chain.append((provider, m))

    other = "Groq" if provider == "Gemini" else "Gemini"
    if resolve_key(other):
        for m in MODELS.get(other, []):
            if not is_quota_exhausted(other, m):
                chain.append((other, m))
    return chain


def _commit_active(provider: str, model: str) -> None:
    """Persist the chosen (provider, model) so the sidebar reflects it after a
    successful fallback, and subsequent calls go straight to it."""
    st.session_state["provider"] = provider
    st.session_state["model"] = model


def _call_one(provider: str, model: str, messages, temperature, json_mode):
    if provider == "Groq":
        return _groq_chat(messages, model, temperature, json_mode)
    return _gemini_chat(messages, model, temperature, json_mode)


def _stream_one(provider: str, model: str, messages, temperature):
    if provider == "Groq":
        yield from _groq_stream(messages, model, temperature)
    else:
        yield from _gemini_stream(messages, model, temperature)


def chat(messages: list[dict], *, model: str | None = None,
         temperature: float = 0.4, json_mode: bool = False) -> str:
    start_p = _provider()
    start_m = model or _model()
    chain = _fallback_chain(start_p, start_m)
    last_err: Exception | None = None

    for i, (p, m) in enumerate(chain):
        try:
            result = _call_one(p, m, messages, temperature, json_mode)
            if (p, m) != (start_p, start_m):
                _notify_fallback(start_p, start_m, p, m)
                _commit_active(p, m)
            return result
        except Exception as e:
            last_err = e
            if not _is_quota_error(e):
                raise
            mark_quota_exhausted(p, m, str(e))
            # try next candidate
            continue

    assert last_err is not None
    raise last_err


def stream_chat(messages: list[dict], *, model: str | None = None,
                temperature: float = 0.6) -> Iterable[str]:
    start_p = _provider()
    start_m = model or _model()

    def _safe_stream():
        chain = _fallback_chain(start_p, start_m)
        last_err: Exception | None = None
        for p, m in chain:
            try:
                # We can't truly "retry mid-stream" once bytes are emitted, but
                # the SDK raises before yielding on quota errors, so the swap
                # works in practice.
                gen = _stream_one(p, m, messages, temperature)
                first = next(gen, None)
                if first is None:
                    if (p, m) != (start_p, start_m):
                        _notify_fallback(start_p, start_m, p, m)
                        _commit_active(p, m)
                    return
                if (p, m) != (start_p, start_m):
                    _notify_fallback(start_p, start_m, p, m)
                    _commit_active(p, m)
                yield first
                yield from gen
                return
            except Exception as e:
                last_err = e
                if not _is_quota_error(e):
                    raise
                mark_quota_exhausted(p, m, str(e))
                continue
        if last_err:
            raise last_err

    return _safe_stream()


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
