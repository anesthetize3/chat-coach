"""Shared sidebar: provider + API key + model selection."""
from __future__ import annotations

import os

import streamlit as st

from lib import llm
from lib.llm import (KEY_ENV_BY_PROVIDER, MODELS, PROVIDERS,
                     _load_from_user_config)


def render() -> None:
    with st.sidebar:
        st.markdown("### ⚙️ Settings")

        provider = st.selectbox(
            "Provider",
            PROVIDERS,
            index=PROVIDERS.index(
                st.session_state.get("provider", llm.DEFAULT_PROVIDER)
            ),
            help="Switch between LLM providers.",
        )
        st.session_state["provider"] = provider

        env_name = KEY_ENV_BY_PROVIDER[provider]
        env_key = os.getenv(env_name, "")
        user_cfg_key = _load_from_user_config(env_name)
        session_key = st.session_state.get(f"{provider.lower()}_key", "")

        if env_key:
            st.markdown(f"<span class='cc-pill ok'>{env_name} loaded (env)</span>",
                        unsafe_allow_html=True)
        elif user_cfg_key:
            st.markdown(
                f"<span class='cc-pill ok'>{env_name} loaded (AppData)</span>",
                unsafe_allow_html=True,
            )
        else:
            key = st.text_input(env_name, type="password",
                                value=session_key,
                                help="Stored only in this session.")
            if key:
                st.session_state[f"{provider.lower()}_key"] = key

        # Model list depends on provider — reset if previous model not valid
        models = MODELS[provider]
        current_model = st.session_state.get("model")
        idx = models.index(current_model) if current_model in models else 0
        st.session_state["model"] = st.selectbox(
            "Model", models, index=idx,
            help="Larger model is more accurate; smaller is faster.",
        )

        st.session_state["language"] = st.selectbox(
            "Language to practice",
            ["English", "Vietnamese"],
            index=1,
            help="Coaching and corrections will be in this language.",
        )

        st.session_state["audience"] = st.selectbox(
            "Audience",
            ["Global / Neutral", "US business", "UK business",
             "Casual peers", "Academic"],
            index=0,
        )
        st.markdown("---")
        st.caption("Nothing is stored to disk. Keys live in env, AppData, "
                   "or this session only.")
