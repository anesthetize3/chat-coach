"""Polish — paste a draft, get side-by-side phrase comparison + recommendations."""
from __future__ import annotations

import html

import streamlit as st

from lib import llm, sidebar, ui

ui.apply("Polish · Chat Coach")
sidebar.render()
ui.hero("✍️ Polish",
        "Side-by-side phrase comparison with comments and recommendations.",
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

SYSTEM = """You are an expert writing coach for the target language stated below.
Compare the user's draft phrase-by-phrase with an improved version, and return
STRICT JSON with these keys:

- "pairs": array aligning the ORIGINAL phrases/sentences to their REVISED versions.
  Each item: {"original": "...", "revised": "...", "comment": "...", "category": "..."}.
  - Split into natural phrases or sentences (NOT individual words).
  - If a phrase is already perfect, "revised" should equal "original" and "comment"
    should briefly say why it works.
  - "comment" must be 1-2 full sentences explaining the change (or non-change),
    referencing grammar, clarity, tone, word choice, or naturalness.
  - "category" is one of: "grammar", "clarity", "tone", "vocabulary", "style", "kept".

- "recommendations": array of 2-5 broader writing tips for the user (each <= 25 words).
  Focus on PATTERNS you noticed. Phrase each as actionable advice.

- "summary": single line summarising the overall change (<= 20 words).

LANGUAGE RULES:
- The draft is in the TARGET LANGUAGE. Keep "original" and "revised" in that language.
- Write all "comment", "recommendations", and "summary" text in the TARGET LANGUAGE
  so the learner reads feedback in the language they are practising.
- For Vietnamese: respect tone particles, classifiers, diacritics, formal vs. casual register.
- For English: respect the requested tone and audience.

Preserve original meaning. Match the requested tone and depth. No prose outside JSON."""


def run_polish(text: str, tone: str, level: str,
               audience: str, language: str) -> dict:
    user = (
        f"TARGET LANGUAGE: {language}\n"
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


CAT_KINDS = {
    "grammar": "err", "clarity": "warn", "tone": "",
    "vocabulary": "ok", "style": "", "kept": "ok",
}

if go:
    if not draft.strip():
        st.warning("Paste some text first.")
        st.stop()
    try:
        with st.spinner("Polishing…"):
            result = run_polish(
                draft.strip(), tone, level,
                st.session_state.get("audience", "Global / Neutral"),
                st.session_state.get("language", "English"),
            )
        st.session_state["polish_result"] = result
        st.session_state["polish_input"] = draft.strip()
    except Exception as e:
        st.error(f"Failed: {e}")
        st.stop()

result = st.session_state.get("polish_result")
if result:
    pairs = result.get("pairs", []) or []
    recs = result.get("recommendations", []) or []
    summary = result.get("summary", "")
    revised_full = " ".join(p.get("revised", "") for p in pairs).strip()

    st.markdown("### Result")
    if summary:
        st.markdown(f"<div class='cc-note'>📝 {summary}</div>",
                    unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(
        ["🔀 Side-by-side", "✨ Clean rewrite", "🎯 Recommendations"]
    )

    with tab1:
        if not pairs:
            st.caption("No phrase comparisons returned.")
        # Header row
        h1, h2, h3 = st.columns([4, 4, 5])
        h1.markdown("**Original**")
        h2.markdown("**Revised**")
        h3.markdown("**Comment**")
        st.markdown("<hr style='margin:6px 0;opacity:0.3'>",
                    unsafe_allow_html=True)

        for p in pairs:
            orig = (p.get("original") or "").strip()
            rev = (p.get("revised") or "").strip()
            comment = (p.get("comment") or "").strip()
            cat = (p.get("category") or "").lower()
            kept = (cat == "kept") or (orig == rev)
            kind = CAT_KINDS.get(cat, "")
            pill = ui.status_pill(
                "Kept" if kept else (cat.title() or "Change"),
                "ok" if kept else kind,
            )

            col1, col2, col3 = st.columns([4, 4, 5])
            with col1:
                bg = "var(--cc-surface-2)" if kept else "rgba(255,107,107,0.08)"
                col1.markdown(
                    f"<div style='background:{bg};padding:10px 12px;"
                    f"border-radius:10px;font-size:0.93rem;line-height:1.5'>"
                    f"{html.escape(orig)}</div>",
                    unsafe_allow_html=True,
                )
            with col2:
                bg = ("var(--cc-surface-2)" if kept
                      else "rgba(52,211,153,0.10)")
                col2.markdown(
                    f"<div style='background:{bg};padding:10px 12px;"
                    f"border-radius:10px;font-size:0.93rem;line-height:1.5'>"
                    f"{html.escape(rev)}</div>",
                    unsafe_allow_html=True,
                )
            with col3:
                col3.markdown(
                    f"<div style='padding:6px 0'>{pill}<br>"
                    f"<span style='font-size:0.9rem;color:var(--cc-muted)'>"
                    f"{html.escape(comment)}</span></div>",
                    unsafe_allow_html=True,
                )
            st.markdown("<div style='height:6px'></div>",
                        unsafe_allow_html=True)

    with tab2:
        st.text_area("Revised", value=revised_full, height=220,
                     label_visibility="collapsed")
        st.download_button("Download .txt", revised_full,
                           file_name="polished.txt")

    with tab3:
        if not recs:
            st.caption("No general recommendations.")
        for i, r in enumerate(recs, 1):
            st.markdown(
                f"<div class='cc-note'><b>{i}.</b> {html.escape(str(r))}</div>",
                unsafe_allow_html=True,
            )
else:
    st.caption("Your polished result will appear here.")
