"""Chat Partner — role-play scenarios with per-turn coaching."""
from __future__ import annotations

import streamlit as st

from lib import llm, sidebar, ui

ui.apply("Chat Partner · Chat Coach")
sidebar.render()
ui.hero("💬 Chat Partner",
        "Role-play a scenario. After each of your messages, get a short coaching note.",
        badge="Chat")

# Show last LLM fallback notice (e.g. Gemini quota → switched to Groq)
_notice = st.session_state.pop("llm_fallback_notice", None)
if _notice:
    st.warning(_notice)

SCENARIOS = {
    "Talking to a woman (dating)": (
        "You are a smart, attractive woman the user just matched with (or met). "
        "You're interested but selective — you notice neediness, low confidence, "
        "boring openers, and try-hard behaviour, and you cool off when you see them. "
        "You warm up when the user is confident, witty, grounded, and curious about "
        "you as a person. Respond naturally as she would. Don't coach the user; "
        "that happens separately. Your speaking style is defined by the PERSONALITY "
        "block, not by this scenario."
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

PERSONALITIES = {
    "Balanced": (
        "Average warmth and openness. Medium-length replies (1-2 sentences). "
        "No strong stylistic skew."
    ),
    "Extrovert (outgoing)": (
        "High energy. Talk A LOT — 2-3 sentences, sometimes more. Use "
        "exclamations, share stories quickly, ask follow-up questions, "
        "use casual slang. Warm up fast if the user matches energy; "
        "get visibly bored and short if he's dry or one-word."
    ),
    "Introvert (reserved)": (
        "VERY short replies — usually 1 sentence, sometimes just a few words. "
        "Don't volunteer information. Wait to be asked. No exclamations, "
        "minimal emojis. Take time to open up; only give longer answers "
        "once the user shows real depth. Cool off if pushed too hard."
    ),
    "Technical / nerdy": (
        "Geeky and direct. Short, dense replies (1-2 sentences). Use "
        "specific, technical vocabulary — drop names of tools, books, "
        "frameworks, concepts. Skip pleasantries and small talk. Get "
        "visibly interested by precise questions; dismiss vague ones with "
        "one-line answers."
    ),
    "Artist / creative": (
        "Expressive and metaphorical. 1-2 sentences but vivid — use sensory "
        "language, comparisons, references to music/film/art/feelings. "
        "Strong opinions, stated with conviction. Roll your eyes at generic "
        "praise or boring office topics."
    ),
    "Rude / blunt": (
        "Sarcastic and impatient. Very short replies (often 1 sentence or a "
        "dry one-liner). Call out boring openers openly ('really? that's "
        "your opener?'). No pleasantries. Dry humour. You DO warm up — "
        "slowly — to someone who holds his frame and pushes back playfully "
        "without crumbling."
    ),
    "Playful / flirty": (
        "Light and teasing. Short replies (1 sentence or a quip). Lots of "
        "playful jabs, emojis sparingly. Reward back-and-forth wit; lose "
        "interest fast at serious, needy, or earnest energy."
    ),
    "Intellectual / philosophical": (
        "Thoughtful and probing. 1-2 considered sentences. Reference ideas, "
        "books, concepts. Answer questions WITH questions sometimes. Don't "
        "accept shallow takes — push back: 'why do you think that?'"
    ),
}

STRICTNESS_LEVELS = {
    "Easy": (
        "Be ENCOURAGING. Most messages rate 3-4/5. Only obviously poor messages "
        "(rude, needy, or grammatically broken) rate 1-2. A 5 is achievable "
        "with any solid, natural message. Lead the explanation with what "
        "works before pointing out one thing to improve."
    ),
    "Normal": (
        "Be FAIR but honest. Baseline is 3/5. A 4 requires confidence and "
        "specificity. A 5 requires confidence, specificity, AND clean grammar. "
        "Call out weaknesses plainly but don't pile on."
    ),
    "Strict": (
        "Be STRICT. Most messages rate 2-3/5. A 4 must be earned with "
        "confidence, wit, AND clean grammar. A 5 is rare — calibrated, "
        "specific, memorable. Call out every weakness."
    ),
    "Brutal": (
        "Be BRUTAL and uncompromising. Most messages rate 1-2/5. A 3 is "
        "above-average. A 4 is exceptional. A 5 is almost never given. "
        "Tear apart every weakness, no sugar-coating. Push him hard."
    ),
}

language = st.session_state.get("language", "English")

with st.container():
    c1, c2, c3 = st.columns([2, 2, 1])
    with c1:
        scenario = st.selectbox("Scenario", list(SCENARIOS),
                                key="scenario_pick")
    with c2:
        personality = st.selectbox("Partner personality",
                                   list(PERSONALITIES),
                                   key="personality_pick")
    with c3:
        st.write("")
        st.write("")
        if st.button("Reset", use_container_width=True):
            for k in ("messages", "active_scenario",
                      "active_language", "active_personality"):
                st.session_state.pop(k, None)
            st.rerun()

    c4, c5, _ = st.columns([2, 2, 1])
    with c4:
        level = st.selectbox("Your level",
                             LEVELS_BY_LANG[language],
                             index=2)
    with c5:
        strictness = st.selectbox("Coach strictness",
                                  list(STRICTNESS_LEVELS),
                                  index=1)  # Normal default

# Reset history when scenario, language, OR personality changes
if (st.session_state.get("active_scenario") != scenario
        or st.session_state.get("active_language") != language
        or st.session_state.get("active_personality") != personality):
    st.session_state["messages"] = []
    st.session_state["active_scenario"] = scenario
    st.session_state["active_language"] = language
    st.session_state["active_personality"] = personality

if "messages" not in st.session_state:
    st.session_state["messages"] = []

PARTNER_SYSTEM = (
    f"You are role-playing a character with this PERSONALITY (most important):\n"
    f"{PERSONALITIES[personality]}\n\n"
    "Your reply length, vocabulary, energy, and topics MUST follow this "
    "personality. If the scenario below conflicts with the personality, the "
    "personality wins.\n\n"
    f"SCENARIO: {SCENARIOS[scenario]}\n\n"
    "Stay fully in character at all times. NEVER break character to coach the "
    "user — coaching is handled separately. NEVER apologise for your tone or "
    "soften it to be helpful; you are not an assistant.\n\n"
    f"TARGET LANGUAGE: {language}. Reply ONLY in {language}. "
    "Use natural register, idioms, and tone particles appropriate to that "
    "language AND to the personality above.\n"
    f"User's {language} level: {level}. Match a natural register; don't "
    "over-simplify.\n\n"
    "HARD STYLE RULES:\n"
    "- Match the reply length specified by the personality (short = SHORT, "
    "  not '4 short sentences').\n"
    "- Do not add disclaimers, niceties, or summaries.\n"
    "- Do not be diplomatic just because the personality is harsh — embody it."
)

COACH_SYSTEM = f"""You are a {language} communication and dating coach for an adult man.
The conversation is conducted in {language}.

COACHING MODE: {strictness}
{STRICTNESS_LEVELS[strictness]}

Your overall job is to make him a more attractive, confident, grounded
communicator — especially in conversations with women.

RATING RUBRIC (default scale, adjusted by COACHING MODE above):
- 1/5: Needy, supplicating, boring, grammatically poor, or generic.
- 2/5: Safe but bland. No personality. Asks generic questions. Hedges a lot.
- 3/5: Clear and grounded but missing spark. Acceptable.
- 4/5: Confident, specific, shows personality, leads the conversation, light wit.
- 5/5: All of the above + grammatically clean, calibrated, and memorable.

Apply the COACHING MODE shift to where you typically land on this rubric.

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

You will also see the user's PREVIOUS messages in this session AND the previous
"fix" you suggested. Use this to spot patterns (repetition, escalating neediness,
dropping frame) AND to recognise when he has taken your advice.

CALIBRATION RULES (critical — apply BEFORE finalising the rating):
1. The "fix" you produce must itself be a 4/5 or 5/5 by the rubric above.
   If the user copies or closely paraphrases your prior "fix", you MUST rate
   AT LEAST 4/5 — your own suggestion can't be a 2/5.
2. If the user took your prior "fix" verbatim with no new flaws, rate 5/5.
3. If he took it and added something good (specificity, wit, personalisation),
   rate 5/5.
4. If he ignored your advice and made the same mistake, rate the same or
   lower than last time and call it out in "explanation".
5. Never penalise a message for being similar to YOUR OWN prior suggestion.
   That's you being inconsistent, not him being unoriginal.

Return STRICT JSON with these keys:
- "rating": integer 1-5, applying the rubric AND the calibration rules above.
- "fix":   ONE rewritten version of his message, IN {language}, demonstrating
           how a grounded, confident man would say it. This "fix" must itself
           qualify as 4/5 or 5/5 — if it wouldn't, write a better one.
           Empty string only if the message is already a 5/5.
- "explanation": 2-4 sentences, IN {language}, explaining what was weak or
                 strong. Reference specific words/phrases. Name the pattern
                 (e.g. "hedging", "needy", "boring opener"). If he took your
                 prior advice, acknowledge it explicitly.
- "synonyms": array of up to 4 objects {{"word": "<weak word he used>", "alternatives": ["stronger1","stronger2","stronger3"]}}.
              Target hedge words, weak verbs, and generic fillers. Words in {language}.
              Empty array if nothing worth replacing.
- "tip":   one short, blunt coaching tip (<= 25 words), IN {language}.
           Tell him what to DO differently next message, not just what was wrong.

No prose outside the JSON. Be respectful of the woman in roleplay scenarios —
strictness is about HIS communication, never about being crude or disrespectful."""


def coach_turn(user_text: str, prior_user_msgs: list[str],
               prior_fix: str = "") -> dict:
    history_block = ""
    if prior_user_msgs:
        joined = "\n".join(f"- {m}" for m in prior_user_msgs[-6:])
        history_block = f"\n\nUser's previous messages this session:\n{joined}"
    prior_fix_block = ""
    if prior_fix:
        prior_fix_block = (
            f"\n\nYOUR PRIOR SUGGESTED FIX (the user may have used it):\n"
            f"\"\"\"\n{prior_fix}\n\"\"\""
        )
    user_payload = (f"Latest message:\n\"\"\"\n{user_text}\n\"\"\""
                    f"{history_block}{prior_fix_block}")
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


SCORE_FACE = {5: "😎", 4: "😊", 3: "😐", 2: "😕", 1: "😬", 0: "🤔"}


def render_coach(coach: dict) -> str:
    rating = int(coach.get("rating", 0) or 0)
    rating = max(0, min(5, rating))
    score_kind = "ok" if rating >= 4 else "warn" if rating == 3 else "err"
    face = SCORE_FACE.get(rating, "🤔")
    face_color = ("var(--cc-ok)" if rating >= 4
                  else "var(--cc-warn)" if rating == 3
                  else "var(--cc-danger)")
    score_pill = (f"<span class='cc-pill {score_kind}' "
                  f"style='font-size:0.95rem;padding:4px 12px'>"
                  f"Score {rating}/5</span>")
    face_html = (
        f"<span style='font-size:2.4rem;line-height:1;"
        f"display:inline-block;vertical-align:middle;"
        f"filter:drop-shadow(0 0 6px {face_color}55);"
        f"margin-right:10px'>{face}</span>"
    )
    score = (f"<div style='display:flex;align-items:center;gap:6px;"
             f"margin:4px 0 8px 0'>{face_html}{score_pill}</div>")
    fix = (coach.get("fix") or "").strip()
    explanation = (coach.get("explanation") or "").strip()
    tip = (coach.get("tip") or "").strip()
    synonyms = coach.get("synonyms") or []

    parts = [f"<b>Coach</b>{score}"]
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
    # Find the most recent prior coach fix (so coach can recognise its own advice)
    prior_fix = ""
    for m in reversed(st.session_state["messages"][:-1]):
        if m["role"] == "user" and m.get("coach"):
            prior_fix = (m["coach"].get("fix") or "").strip()
            if prior_fix:
                break
    with st.chat_message("user"):
        coach_slot = st.empty()
        coach_slot.markdown(
            "<div class='cc-note'>🧠 <i>Coach is thinking…</i></div>",
            unsafe_allow_html=True,
        )
        try:
            coach = coach_turn(prompt, prior_user_msgs, prior_fix)
        except Exception as e:
            coach_slot.error(f"Coach failed: {e}")
            coach = {"rating": 0, "fix": "", "explanation": "",
                     "synonyms": [], "tip": ""}
        coach_slot.markdown(render_coach(coach), unsafe_allow_html=True)
    st.session_state["messages"][-1]["coach"] = coach

    # Partner reply (streamed)
    history = [{"role": "system", "content": PARTNER_SYSTEM}] + [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state["messages"]
    ]
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown(
            "<span style='color:var(--cc-muted)'>💭 <i>Typing…</i></span>",
            unsafe_allow_html=True,
        )
        acc = ""
        try:
            for piece in llm.stream_chat(history, temperature=0.9):
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
