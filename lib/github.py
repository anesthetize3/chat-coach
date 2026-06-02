"""GitHub REST API wrapper for the Feedback feature.

Stores feedback as GitHub Issues in the configured repo. Requires a
Personal Access Token with `repo` scope (private) or `public_repo` (public).

Token resolution: GITHUB_TOKEN env → session state → %APPDATA%/chat-coach-v2/.env
"""
from __future__ import annotations

import os
from typing import Any

import requests
import streamlit as st

from lib.llm import _load_from_user_config

REPO_OWNER = "anesthetize3"
REPO_NAME = "chat-coach"
API = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"

FEEDBACK_LABEL = "feedback"
TYPE_LABELS = {"bug": "bug", "feature": "enhancement", "feedback": "feedback"}
STATUS_LABELS = {"done": "done", "rejected": "rejected"}


def resolve_token() -> str:
    return (
        os.getenv("GITHUB_TOKEN")
        or st.session_state.get("github_token", "")
        or _load_from_user_config("GITHUB_TOKEN")
    )


def _headers() -> dict:
    token = resolve_token()
    if not token:
        raise RuntimeError(
            "Missing GITHUB_TOKEN. Add a Personal Access Token in the "
            "sidebar, .env, or %APPDATA%/chat-coach-v2/.env."
        )
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def _check(resp: requests.Response) -> Any:
    if not resp.ok:
        raise RuntimeError(f"GitHub {resp.status_code}: {resp.text[:300]}")
    return resp.json() if resp.text else {}


def list_issues(state: str = "open") -> list[dict]:
    """state = open | closed | all. Filters to feedback-labeled issues only."""
    resp = requests.get(
        f"{API}/issues",
        headers=_headers(),
        params={"state": state, "labels": FEEDBACK_LABEL,
                "per_page": 50, "sort": "created", "direction": "desc"},
        timeout=15,
    )
    issues = _check(resp)
    return [i for i in issues if "pull_request" not in i]


def create_issue(title: str, body: str, kind: str) -> dict:
    labels = [FEEDBACK_LABEL]
    extra = TYPE_LABELS.get(kind)
    if extra and extra not in labels:
        labels.append(extra)
    resp = requests.post(
        f"{API}/issues",
        headers=_headers(),
        json={"title": title, "body": body, "labels": labels},
        timeout=15,
    )
    return _check(resp)


def list_comments(issue_number: int) -> list[dict]:
    resp = requests.get(
        f"{API}/issues/{issue_number}/comments",
        headers=_headers(), timeout=15,
    )
    return _check(resp)


def add_comment(issue_number: int, body: str) -> dict:
    resp = requests.post(
        f"{API}/issues/{issue_number}/comments",
        headers=_headers(), json={"body": body}, timeout=15,
    )
    return _check(resp)


def _patch_issue(issue_number: int, payload: dict) -> dict:
    resp = requests.patch(
        f"{API}/issues/{issue_number}",
        headers=_headers(), json=payload, timeout=15,
    )
    return _check(resp)


def close_issue(issue_number: int, reason: str = "done") -> dict:
    """reason: 'done' or 'rejected' — added as label, plus close state."""
    # First add the status label
    if reason in STATUS_LABELS:
        requests.post(
            f"{API}/issues/{issue_number}/labels",
            headers=_headers(),
            json={"labels": [STATUS_LABELS[reason]]},
            timeout=15,
        )
    state_reason = "completed" if reason == "done" else "not_planned"
    return _patch_issue(issue_number, {"state": "closed",
                                       "state_reason": state_reason})


def reopen_issue(issue_number: int) -> dict:
    return _patch_issue(issue_number, {"state": "open"})
