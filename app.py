"""Chat Coach v2 — modernized Streamlit app. Landing page."""
from __future__ import annotations

import streamlit as st

from lib import ui

ui.apply("Chat Coach")
ui.hero(
    "Speak English with confidence.",
    "A focused coach that polishes your writing and rehearses real conversations.",
    badge="v2 · powered by Groq",
)

c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        "<div class='cc-card'>"
        "<h4>✍️ Polish</h4>"
        "<p>Paste any draft — email, message, post. Get a side-by-side phrase "
        "comparison plus comments and recommendations.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Open Polish →", use_container_width=True, type="primary"):
        st.switch_page("pages/1_Polish.py")

with c2:
    st.markdown(
        "<div class='cc-card'>"
        "<h4>💬 Chat Partner</h4>"
        "<p>Practice real conversations — including talking to a woman. "
        "Get a strict per-turn coaching note that pushes you to be sharper.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Open Chat Partner →", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Chat.py")

with c3:
    st.markdown(
        "<div class='cc-card'>"
        "<h4>🐛 Feedback</h4>"
        "<p>Report bugs or request features. Stored as GitHub Issues so you "
        "can reply, close, or reject them right here.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Open Feedback →", use_container_width=True, type="primary"):
        st.switch_page("pages/3_Feedback.py")

st.write("")
st.markdown(
    "<div class='cc-note'>Tip: set <code>GROQ_API_KEY</code> in a <code>.env</code> file "
    "next to <code>app.py</code>, or paste it in the sidebar of any page.</div>",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Chat Coach")
    st.caption("Modernized v2 — Polish + Chat")
    st.markdown("---")
    st.caption("Choose a page above ☝️")
