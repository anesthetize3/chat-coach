"""Feedback & Bugs — submit and manage issues via GitHub Issues."""
from __future__ import annotations

import os
from datetime import datetime

import streamlit as st

from lib import github, sidebar, ui
from lib.llm import _load_from_user_config

ui.apply("Feedback · Chat Coach")
sidebar.render()
ui.hero("🐛 Feedback & Bugs",
        "Report bugs, request features, and track responses. Stored as GitHub Issues.",
        badge="Feedback")


# ---------------- GitHub token block ----------------

with st.sidebar:
    st.markdown("### 🐙 GitHub")
    env_tok = os.getenv("GITHUB_TOKEN", "")
    cfg_tok = _load_from_user_config("GITHUB_TOKEN")
    if env_tok:
        st.markdown("<span class='cc-pill ok'>GITHUB_TOKEN loaded (env)</span>",
                    unsafe_allow_html=True)
    elif cfg_tok:
        st.markdown("<span class='cc-pill ok'>GITHUB_TOKEN loaded (AppData)</span>",
                    unsafe_allow_html=True)
    else:
        tok = st.text_input(
            "GITHUB_TOKEN", type="password",
            value=st.session_state.get("github_token", ""),
            help="Personal Access Token with 'repo' scope. "
                 "Create at github.com/settings/tokens",
        )
        if tok:
            st.session_state["github_token"] = tok
    st.caption(f"Repo: {github.REPO_OWNER}/{github.REPO_NAME}")

if not github.resolve_token():
    st.warning("Add a GitHub Personal Access Token in the sidebar to use this page. "
               "Create one at https://github.com/settings/tokens (scope: `repo`).")
    st.stop()


# ---------------- Tabs ----------------

tab_submit, tab_browse = st.tabs(["✍️ Submit", "📋 Browse & manage"])

# ===== Submit =====

with tab_submit:
    st.markdown("#### New report")
    with st.form("new_report", clear_on_submit=True):
        kind = st.selectbox("Type",
                            ["bug", "feature", "feedback"],
                            format_func=lambda k: {"bug": "🐛 Bug",
                                                   "feature": "✨ Feature request",
                                                   "feedback": "💬 General feedback"}[k])
        title = st.text_input("Title", placeholder="One-line summary")
        body = st.text_area(
            "Details", height=160,
            placeholder=("Steps to reproduce, expected vs. actual, screenshots, "
                         "or any context that helps."),
        )
        submitted = st.form_submit_button("Submit", type="primary")

    if submitted:
        if not title.strip() or not body.strip():
            st.error("Title and details are both required.")
        else:
            full_body = (
                f"{body.strip()}\n\n---\n"
                f"_Submitted via Chat Coach at "
                f"{datetime.utcnow().isoformat(timespec='seconds')}Z_"
            )
            try:
                issue = github.create_issue(title.strip(), full_body, kind)
                st.success(f"Created [#{issue['number']}]({issue['html_url']})")
            except Exception as e:
                st.error(f"Failed: {e}")

# ===== Browse =====

with tab_browse:
    c1, c2 = st.columns([3, 1])
    with c1:
        state = st.radio("Filter", ["open", "closed", "all"],
                         horizontal=True, index=0,
                         label_visibility="collapsed")
    with c2:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()

    try:
        issues = github.list_issues(state=state)
    except Exception as e:
        st.error(f"Failed to load issues: {e}")
        issues = []

    if not issues:
        st.caption("No issues to show.")

    for issue in issues:
        num = issue["number"]
        title = issue["title"]
        state_now = issue["state"]
        labels = [lb["name"] for lb in issue.get("labels", [])]
        status_kind = ("ok" if "done" in labels
                       else "err" if "rejected" in labels
                       else "warn" if state_now == "open" else "")
        status_text = ("Done" if "done" in labels
                       else "Rejected" if "rejected" in labels
                       else "Open" if state_now == "open" else "Closed")
        type_label = next((lb for lb in labels
                           if lb in {"bug", "enhancement", "feedback"}), "")
        type_pill = (ui.status_pill(type_label, "") if type_label else "")
        status_pill = ui.status_pill(status_text, status_kind)
        header = f"#{num} · {title}"

        with st.expander(header, expanded=False):
            st.markdown(f"{status_pill} &nbsp; {type_pill} &nbsp; "
                        f"<a href='{issue['html_url']}' target='_blank'>"
                        f"open on GitHub ↗</a>",
                        unsafe_allow_html=True)
            body = issue.get("body") or "_(no description)_"
            st.markdown(body)

            # Comments
            try:
                comments = github.list_comments(num)
            except Exception as e:
                comments = []
                st.warning(f"Couldn't load comments: {e}")
            if comments:
                st.markdown("**Replies**")
            for c in comments:
                author = c["user"]["login"]
                created = c["created_at"][:10]
                st.markdown(
                    f"<div class='cc-note'><b>@{author}</b> "
                    f"<span class='cc-muted'>· {created}</span><br>"
                    f"{c['body']}</div>",
                    unsafe_allow_html=True,
                )

            # Reply box
            reply = st.text_area("Reply", key=f"reply_{num}",
                                 height=80, label_visibility="collapsed",
                                 placeholder="Write a reply…")
            ac1, ac2, ac3, ac4 = st.columns(4)
            with ac1:
                if st.button("💬 Reply", key=f"btn_reply_{num}",
                             use_container_width=True):
                    if reply.strip():
                        try:
                            github.add_comment(num, reply.strip())
                            st.success("Reply posted.")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Failed: {e}")
                    else:
                        st.warning("Empty reply.")
            with ac2:
                if state_now == "open" and st.button(
                        "✅ Mark done", key=f"btn_done_{num}",
                        use_container_width=True):
                    try:
                        github.close_issue(num, "done")
                        st.success("Closed as done.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed: {e}")
            with ac3:
                if state_now == "open" and st.button(
                        "🚫 Reject", key=f"btn_reject_{num}",
                        use_container_width=True):
                    try:
                        github.close_issue(num, "rejected")
                        st.success("Closed as rejected.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed: {e}")
            with ac4:
                if state_now == "closed" and st.button(
                        "↩️ Reopen", key=f"btn_reopen_{num}",
                        use_container_width=True):
                    try:
                        github.reopen_issue(num)
                        st.success("Reopened.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Failed: {e}")
