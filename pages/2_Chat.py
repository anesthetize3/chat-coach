"""Chat Partner — role-play scenarios with per-turn coaching."""
from __future__ import annotations

import streamlit as st

from lib import llm, sidebar, ui

ui.apply("Chat Partner · Chat Coach")
sidebar.render()
ui.hero("💬 Chat Partner",
        "Role-play a scenario. After each of your messages, get a short coaching note.",
        badge="Chat")

SCENARIOS = {
    "Job interview": "You are a friendly senior hiring manager interviewing the user for a software role. Ask one question at a time.",
    "Daily standup": "You are a teammate at a standup. Ask the user about yesterday, today, blockers — naturally.",
    "Small talk (coffee)": "You are a colleague chatting casually before a meeting. Keep it warm and light.",
    "Customer support call": "You are a customer with a billing issue. Be polite but slightly frustrated.",
    "1:1 with manager": "You are the user's manager in a 1:1. Be supportive, ask thoughtful questions.",
    "Negotiation": "You are a vendor negotiating a contract renewal. Push back firmly but fairly.",
}

LEVELS_BY_LANG = {
    "English": ["A2 Elementary", "B1 Intermediate",
                "B2 Upper-Intermediate", "C1 Advanced"],
    "Vietnamese": ["Beginner (sơ cấp)", "Intermediate (trung cấp)",
                   "Upper-Intermediate (trung cao)", "Advanced (cao cấp)"],
}

language = st.session_state.get("language", "English")

with st.container():
    c1, c2, c3 = st.columns([2, 2, 1])
    with c1:
        scenario = st.selectbox("Scenario", list(SCENARIOS),
                                key="scenario_pick")
    with c2:
        level = st.selectbox("Your level",
                             LEVELS_BY_LANG[language],
                             index=2)
    with c3:
        st.write("")
        st.write("")
        if st.button("Reset", use_container_width=True):
            for k in ("messages", "active_scenario", "active_language"):
                st.session_state.pop(k, None)
            st.rerun()

# Reset history when scenario OR language changes
if (st.session_state.get("active_scenario") != scenario
        or st.session_state.get("active_language") != language):
    st.session_state["messages"] = []
    st.session_state["active_scenario"] = scenario
    st.session_state["active_language"] = language

if "messages" not in st.session_state:
    st.session_state["messages"] = []

PARTNER_SYSTEM = (
    "You are role-playing in the following scenario. Stay fully in character. "
    "Keep replies to 1–3 sentences. Don't break character to coach — coaching is handled separately.\n\n"
    f"Scenario: {SCENARIOS[scenario]}\n"
    f"TARGET LANGUAGE: {language}. Reply ONLY in {language}. "
    "Use natural register, idioms, and tone particles appropriate to that language.\n"
    f"User's {language} level: {level}. Match a natural register; don't over-simplify."
)

COACH_SYSTEM = f"""You are a {language} language coach analysing the user's latest message
in a conversation. The conversation is conducted in {language}.
You will also see the user's PREVIOUS messages in this session so you can spot repeated
or overused words.

Return STRICT JSON with these keys:
- "rating": integer 1-5 (overall quality of this message: grammar, clarity, naturalness)
- "fix":   a single corrected, more natural version of the message, IN {language}.
           Empty string if no change is needed.
- "explanation": 2-4 sentences, IN {language}, explaining WHY you suggested the fix.
                 Reference specific words/phrases. Cover grammar, word choice, register,
                 or naturalness. If the message is already good, explain what makes it work.
- "synonyms": array of up to 4 objects {{"word": "<word user used>", "alternatives": ["alt1","alt2","alt3"]}}.
              Words and alternatives must be in {language}.
              Prioritise words the user has REPEATED across messages, then generic/overused
              words in {language}. Empty array if nothing worth replacing.
- "tip":   one short, actionable coaching tip (<= 22 words), IN {language}.

No prose outside the JSON. Be concrete and kind."""


def coach_turn(user_text: str, prior_user_msgs: list[str]) -> dict:
    history_block = ""
    if prior_user_msgs:
        joined = "\n".join(f"- {m}" for m in prior_user_msgs[-6:])
        history_block = f"\n\nUser's previous messages this session:\n{joined}"
    user_payload = f"Latest message:\n\"\"\"\n{user_text}\n\"\"\"{history_block}"
    raw = llm.chat(
        [{"role": "system", "content": COACH_SYSTEM},
         {"role": "user", "content": user_payload}],
        temperature=0.2,
        json_mode=True,
    )
    try:
        return llm.parse_json(raw)
    except Exception:
        return {"rating": 0, "fix": "", "explanation": "",
                "synonyms": [], "tip": ""}


def render_coach(coach: dict) -> str:
    rating = int(coach.get("rating", 0) or 0)
    score_kind = "ok" if rating >= 4 else "warn" if rating == 3 else "err"
    score = (f"<span class='cc-pill {score_kind}'>"
             f"Score {rating}/5</span>")
    fix = (coach.get("fix") or "").strip()
    explanation = (coach.get("explanation") or "").strip()
    tip = (coach.get("tip") or "").strip()
    synonyms = coach.get("synonyms") or []

    parts = [f"<b>Coach</b> &nbsp; {score}"]
    if fix:
        parts.append(f"<br><b>Try:</b> <i>{fix}</i>")
    if explanation:
        parts.append(f"<br><b>Why:</b> {explanation}")
    if synonyms:
        rows = []
        for s in synonyms[:4]:
            w = (s.get("word") or "").strip()
            alts = s.get("alternatives") or []
            if not w or not alts:
                continue
            alt_pills = " ".join(
                f"<span class='cc-pill'>{a}</span>" for a in alts[:4]
            )
            rows.append(f"<div style='margin:3px 0'>"
                        f"<code>{w}</code> → {alt_pills}</div>")
        if rows:
            parts.append("<br><b>Word swaps:</b>" + "".join(rows))
    if tip:
        parts.append(f"<br>💡 {tip}")
    return "<div class='cc-note'>" + "".join(parts) + "</div>"


# Render history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("coach"):
            st.markdown(render_coach(msg["coach"]), unsafe_allow_html=True)

prompt = st.chat_input("Type your reply…")
if prompt:
    st.session_state["messages"].append(
        {"role": "user", "content": prompt, "coach": None}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # Coach (non-streamed) — pass prior user messages so it can spot repetition
    prior_user_msgs = [m["content"] for m in st.session_state["messages"][:-1]
                       if m["role"] == "user"]
    try:
        coach = coach_turn(prompt, prior_user_msgs)
    except Exception as e:
        st.error(f"Coach failed: {e}")
        coach = {"rating": 0, "fix": "", "explanation": "",
                 "synonyms": [], "tip": ""}
    st.session_state["messages"][-1]["coach"] = coach

    # Show coach immediately under user msg
    with st.chat_message("user"):
        st.markdown(render_coach(coach), unsafe_allow_html=True)

    # Partner reply (streamed)
    history = [{"role": "system", "content": PARTNER_SYSTEM}] + [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state["messages"]
    ]
    with st.chat_message("assistant"):
        placeholder = st.empty()
        acc = ""
        try:
            for piece in llm.stream_chat(history, temperature=0.7):
                acc += piece
                placeholder.markdown(acc + "▌")
            placeholder.markdown(acc)
        except Exception as e:
            placeholder.error(f"Partner failed: {e}")
            acc = ""
    if acc:
        st.session_state["messages"].append(
            {"role": "assistant", "content": acc, "coach": None}
        )

if not st.session_state["messages"]:
    st.caption("Pick a scenario above and send your first message to start.")
