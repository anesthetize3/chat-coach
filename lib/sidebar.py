"""Shared sidebar: API key + model selection."""
from __future__ import annotations

import os

import streamlit as st

from lib.llm import DEFAULT_MODEL, FALLBACK_MODEL, _load_from_user_config


def render() -> None:
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        env_key = os.getenv("GROQ_API_KEY", "")
        user_cfg_key = _load_from_user_config()
        if env_key:
            st.markdown("<span class='cc-pill ok'>API key loaded (env)</span>",
                        unsafe_allow_html=True)
        elif user_cfg_key:
            st.markdown(
                "<span class='cc-pill ok'>API key loaded (AppData)</span>",
                unsafe_allow_html=True,
            )
        else:
            key = st.text_input("GROQ_API_KEY", type="password",
                                value=st.session_state.get("groq_key", ""),
                                help="Stored only in this session.")
            if key:
                st.session_state["groq_key"] = key

        st.session_state["model"] = st.selectbox(
            "Model",
            [DEFAULT_MODEL, FALLBACK_MODEL],
            index=0,
            help="Larger model is more accurate; smaller is faster.",
        )

        st.session_state["language"] = st.selectbox(
            "Language to practice",
            ["English", "Vietnamese"],
            index=0,
            help="Coaching and corrections will be in this language.",
        )

        st.session_state["audience"] = st.selectbox(
            "Audience",
            ["Global / Neutral", "US business", "UK business",
             "Casual peers", "Academic"],
            index=0,
        )
        st.markdown("---")
        st.caption("All processing happens via the Groq API. "
                   "Nothing is stored to disk.")
