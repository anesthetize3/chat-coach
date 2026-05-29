"""Groq LLM client wrapper. Reads GROQ_API_KEY from env or .env."""
from __future__ import annotations

import json
import os
from typing import Iterable

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

DEFAULT_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"


def _client():
    from groq import Groq
    key = os.getenv("GROQ_API_KEY") or st.session_state.get("groq_key", "")
    if not key:
        raise RuntimeError("Missing GROQ_API_KEY. Set it in .env or Settings.")
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
