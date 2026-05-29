"""Diff rendering: word-level inline diff for Polish."""
from __future__ import annotations

import difflib
import html


def inline_diff(original: str, revised: str) -> str:
    a = original.split()
    b = revised.split()
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    out: list[str] = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        chunk_a = html.escape(" ".join(a[i1:i2]))
        chunk_b = html.escape(" ".join(b[j1:j2]))
        if tag == "equal":
            out.append(chunk_a)
        elif tag == "replace":
            out.append(f"<del>{chunk_a}</del> <ins>{chunk_b}</ins>")
        elif tag == "delete":
            out.append(f"<del>{chunk_a}</del>")
        elif tag == "insert":
            out.append(f"<ins>{chunk_b}</ins>")
        out.append(" ")
    return "".join(out).strip()
