"""Polish — paste a draft, get fixes, rewrite, and notes."""
from __future__ import annotations

import streamlit as st

from lib import llm, sidebar, ui
from lib.diff import inline_diff

ui.apply("Polish · Chat Coach")
sidebar.render()
ui.hero("✍️ Polish",
        "Inline diff, clean rewrite, and short coaching notes.",
        badge="Polish")

TONES = ["Keep tone", "More professional", "Friendlier", "More concise",
         "More confident", "More diplomatic"]
LEVELS = ["Light (grammar only)", "Standard (grammar + clarity)",
          "Deep (rewrite for impact)"]

c1, c2, c3 = st.columns([2, 2, 1])
with c1:
    tone = st.selectbox("Tone", TONES, index=0)
with c2:
    level = st.selectbox("Depth", LEVELS, index=1)
with c3:
    st.write("")
    st.write("")
    go = st.button("Polish", type="primary", use_container_width=True)

draft = st.text_area(
    "Your draft",
    height=200,
    placeholder="Paste an email, message, or paragraph…",
    key="draft",
)

SYSTEM = """You are an expert English writing coach. Return STRICT JSON with keys:
- "revised": the rewritten text (string)
- "notes": array of objects {category, comment} where category is one of
  ["grammar","clarity","tone","vocabulary","style"], 2-5 items, each comment <= 22 words
- "summary": one-line summary of changes (<= 18 words)
No prose outside JSON. Preserve original meaning and language register requested by the user."""


def run_polish(text: str, tone: str, level: str, audience: str) -> dict:
    user = (
        f"Audience: {audience}\nTone preference: {tone}\nDepth: {level}\n\n"
        f"Draft:\n\"\"\"\n{text}\n\"\"\""
    )
    raw = llm.chat(
        [{"role": "system", "content": SYSTEM},
         {"role": "user", "content": user}],
        temperature=0.3,
        json_mode=True,
    )
    return llm.parse_json(raw)


if go:
    if not draft.strip():
        st.warning("Paste some text first.")
        st.stop()
    try:
        with st.spinner("Polishing…"):
            result = run_polish(
                draft.strip(), tone, level,
                st.session_state.get("audience", "Global / Neutral"),
            )
        st.session_state["polish_result"] = result
        st.session_state["polish_input"] = draft.strip()
    except Exception as e:
        st.error(f"Failed: {e}")
        st.stop()

result = st.session_state.get("polish_result")
if result:
    original = st.session_state.get("polish_input", "")
    revised = result.get("revised", "").strip()
    notes = result.get("notes", [])
    summary = result.get("summary", "")

    st.markdown("### Result")
    if summary:
        st.markdown(f"<div class='cc-note'>📝 {summary}</div>",
                    unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔀 Diff", "✨ Clean rewrite", "🎯 Notes"])
    with tab1:
        st.markdown(
            f"<div class='cc-diff'>{inline_diff(original, revised)}</div>",
            unsafe_allow_html=True,
        )
        st.caption("Red strikethrough = removed · Green = added")
    with tab2:
        st.text_area("Revised", value=revised, height=220,
                     label_visibility="collapsed")
        st.download_button("Download .txt", revised, file_name="polished.txt")
    with tab3:
        if not notes:
            st.caption("No notes returned.")
        cat_kinds = {"grammar": "err", "clarity": "warn",
                     "tone": "", "vocabulary": "ok", "style": ""}
        for n in notes:
            cat = (n.get("category") or "").lower()
            kind = cat_kinds.get(cat, "")
            pill = ui.status_pill(cat.title() or "Note", kind)
            st.markdown(
                f"<div class='cc-note'>{pill} &nbsp; {n.get('comment','')}</div>",
                unsafe_allow_html=True,
            )
else:
    st.caption("Your polished result will appear here.")
