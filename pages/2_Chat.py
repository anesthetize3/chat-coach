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
    "Talking to a woman (dating)": (
        "You are a smart, attractive woman the user just matched with (or met). "
        "You're interested but selective — you notice neediness, low confidence, "
        "boring openers, and try-hard behaviour, and you cool off when you see them. "
        "You warm up when the user is confident, witty, grounded, and curious about "
        "you as a person. Stay in character, respond naturally as she would — short, "
        "playful, sometimes teasing. Don't coach the user; that happens separately."
    ),
    "Daily standup": "You are a teammate at a standup. Ask the user about yesterday, today, blockers — naturally.",
    "Small talk (coffee)": "You are a colleague chatting casually before a meeting. Keep it warm and light.",
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

COACH_SYSTEM = f"""You are a STRICT {language} communication and dating coach for an adult man.
The conversation is conducted in {language}.

Your job is to make him a more attractive, confident, grounded communicator —
especially in conversations with women. Be honest, direct, and demanding.
Most messages should rate 2-3/5. Only genuinely strong messages earn 4. A 5
is rare and reserved for messages that are both grammatically clean AND
demonstrate calibrated confidence, wit, and intentionality.

RATING RUBRIC (be strict):
- 1/5: Needy, supplicating, boring, grammatically poor, or generic.
- 2/5: Safe but bland. No personality. Asks generic questions. Hedges a lot.
- 3/5: Clear and grounded but missing spark. Acceptable.
- 4/5: Confident, specific, shows personality, leads the conversation, light wit.
- 5/5: All of the above + grammatically clean, calibrated, and memorable.

PENALISE HARD (must be called out in "explanation" when present):
- Excessive hedging: "maybe", "sorry to bother", "I was just wondering", "if you don't mind"
- Over-apologising or seeking permission/validation
- Compliments on appearance too early ("you're so beautiful")
- Boring openers: "Hi", "Hey how are you", "How was your day?" with no hook
- Long monologues / over-explaining
- Asking too many questions in a row (interview mode)
- Trying too hard to impress (humble-brags, flexing)
- People-pleasing, agreeing with everything she says
- Emoji-spam or excessive exclamation marks
- Negging, insults, sexual escalation too early, or anything disrespectful (also penalise)

REWARD:
- Statements over questions (or pair a statement with a question)
- Specific observations (not generic compliments)
- Playful teasing that is warm, not mean
- Holding a frame: not collapsing when teased back
- Showing you have a life: hobbies, opinions, plans
- Brevity. 1-3 sentences usually beats a paragraph.
- Curiosity about her as a person, not her looks

You will also see the user's PREVIOUS messages this session to spot patterns
(repetition, escalating neediness, dropping frame, etc.).

Return STRICT JSON with these keys:
- "rating": integer 1-5, applying the rubric above honestly.
- "fix":   ONE rewritten version of his message, IN {language}, demonstrating
           how a grounded, confident man would say it. Empty string only if
           the message is already a 5/5.
- "explanation": 2-4 sentences, IN {language}, explaining what was weak or
                 strong. Reference specific words/phrases. Name the pattern
                 (e.g. "hedging", "needy", "boring opener"). If the message
                 is solid, say specifically what works and don't soften the
                 critique of the remaining weak parts.
- "synonyms": array of up to 4 objects {{"word": "<weak word he used>", "alternatives": ["stronger1","stronger2","stronger3"]}}.
              Target hedge words, weak verbs, and generic fillers. Words in {language}.
              Empty array if nothing worth replacing.
- "tip":   one short, blunt coaching tip (<= 25 words), IN {language}.
           Tell him what to DO differently next message, not just what was wrong.

No prose outside the JSON. Be respectful of the woman in roleplay scenarios —
strictness is about HIS communication, never about being crude or disrespectful."""


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
