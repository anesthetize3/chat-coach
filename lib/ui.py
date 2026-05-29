"""Shared UI: theme, CSS, layout helpers."""
from __future__ import annotations

import streamlit as st

CSS = """
<style>
:root {
  --cc-bg: #0b0d12;
  --cc-surface: #11141b;
  --cc-surface-2: #161a24;
  --cc-border: #232838;
  --cc-text: #e7ebf3;
  --cc-muted: #8a93a6;
  --cc-accent: #7c9cff;
  --cc-accent-2: #5eead4;
  --cc-danger: #ff6b6b;
  --cc-warn: #fbbf24;
  --cc-ok: #34d399;
  --cc-radius: 14px;
}
@media (prefers-color-scheme: light) {
  :root {
    --cc-bg: #f7f8fb;
    --cc-surface: #ffffff;
    --cc-surface-2: #f1f3f8;
    --cc-border: #e3e7ef;
    --cc-text: #0f1320;
    --cc-muted: #5b6478;
    --cc-accent: #3a5cff;
    --cc-accent-2: #0ea5e9;
  }
}
html, body, [data-testid="stAppViewContainer"] {
  background: var(--cc-bg);
  color: var(--cc-text);
}
[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2.2rem; max-width: 1080px; }
h1, h2, h3, h4 { color: var(--cc-text); letter-spacing: -0.01em; }
.cc-hero {
  padding: 28px 28px 24px;
  border-radius: var(--cc-radius);
  background: linear-gradient(135deg, rgba(124,156,255,0.10), rgba(94,234,212,0.08));
  border: 1px solid var(--cc-border);
  margin-bottom: 22px;
}
.cc-hero h1 { font-size: 2.0rem; margin: 0 0 6px 0; }
.cc-hero p { color: var(--cc-muted); margin: 0; font-size: 1.02rem; }
.cc-badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 4px 10px; border-radius: 999px;
  background: rgba(124,156,255,0.12); color: var(--cc-accent);
  font-size: 0.78rem; font-weight: 600; letter-spacing: 0.02em;
  margin-bottom: 12px; border: 1px solid rgba(124,156,255,0.25);
}
.cc-card {
  background: var(--cc-surface);
  border: 1px solid var(--cc-border);
  border-radius: var(--cc-radius);
  padding: 20px 20px 18px;
  transition: transform .15s ease, border-color .15s ease;
  height: 100%;
}
.cc-card:hover { border-color: var(--cc-accent); transform: translateY(-2px); }
.cc-card h4 { margin: 0 0 6px 0; font-size: 1.05rem; }
.cc-card p { color: var(--cc-muted); margin: 0; font-size: 0.92rem; line-height: 1.5; }
.cc-pill {
  display: inline-block; padding: 2px 9px; border-radius: 999px;
  font-size: 0.72rem; font-weight: 600;
  background: var(--cc-surface-2); color: var(--cc-muted);
  border: 1px solid var(--cc-border);
}
.cc-pill.ok    { color: var(--cc-ok);    border-color: rgba(52,211,153,0.4); }
.cc-pill.warn  { color: var(--cc-warn);  border-color: rgba(251,191,36,0.4); }
.cc-pill.err   { color: var(--cc-danger);border-color: rgba(255,107,107,0.4); }

.cc-diff {
  background: var(--cc-surface);
  border: 1px solid var(--cc-border);
  border-radius: var(--cc-radius);
  padding: 16px 18px;
  font-size: 0.98rem;
  line-height: 1.6;
}
.cc-diff ins { background: rgba(52,211,153,0.18); color: var(--cc-ok); text-decoration: none; padding: 0 2px; border-radius: 3px;}
.cc-diff del { background: rgba(255,107,107,0.16); color: var(--cc-danger); text-decoration: line-through; padding: 0 2px; border-radius: 3px;}

.cc-note {
  background: var(--cc-surface-2);
  border-left: 3px solid var(--cc-accent);
  padding: 10px 14px; border-radius: 8px;
  color: var(--cc-text); font-size: 0.93rem;
  margin: 6px 0;
}
.cc-muted { color: var(--cc-muted); font-size: 0.88rem; }

[data-testid="stSidebar"] { background: var(--cc-surface); border-right: 1px solid var(--cc-border); }
.stButton > button {
  border-radius: 10px; border: 1px solid var(--cc-border);
  background: var(--cc-surface-2); color: var(--cc-text);
  padding: 0.5rem 1rem; font-weight: 600;
}
.stButton > button:hover { border-color: var(--cc-accent); color: var(--cc-accent); }
.stButton > button[kind="primary"] {
  background: var(--cc-accent); color: white; border-color: var(--cc-accent);
}
.stButton > button[kind="primary"]:hover { filter: brightness(1.08); color: white; }
textarea, input { border-radius: 10px !important; }
[data-testid="stChatMessage"] { background: var(--cc-surface); border: 1px solid var(--cc-border); border-radius: var(--cc-radius); }
</style>
"""


def apply(title: str = "Chat Coach") -> None:
    st.set_page_config(page_title=title, page_icon="💬", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)


def hero(title: str, subtitle: str, badge: str | None = None) -> None:
    badge_html = f"<div class='cc-badge'>● {badge}</div>" if badge else ""
    st.markdown(
        f"<div class='cc-hero'>{badge_html}<h1>{title}</h1><p>{subtitle}</p></div>",
        unsafe_allow_html=True,
    )


def status_pill(label: str, kind: str = "") -> str:
    return f"<span class='cc-pill {kind}'>{label}</span>"
