from __future__ import annotations
from typing import Sequence
import re

def keyword_hits(text: str, keywords: Sequence[str]) -> dict[str, int]:
    text_l = text.lower()
    return {k: len(re.findall(re.escape(k.lower()), text_l)) for k in keywords}

def score_abstract(text: str, keywords: Sequence[str], weights: dict[str, float] | None = None) -> float:
    hits = keyword_hits(text, keywords)
    weights = weights or {k: 1.0 for k in keywords}
    return float(sum(hits[k] * weights.get(k, 1.0) for k in keywords))

def rank_papers(papers: list[dict], keywords: Sequence[str], weights: dict[str, float] | None = None) -> list[dict]:
    out = []
    for p in papers:
        text = f"{p.get('title','')} {p.get('abstract','')}"
        s = score_abstract(text, keywords, weights)
        row = dict(p)
        row["score"] = s
        out.append(row)
    return sorted(out, key=lambda x: -x["score"])
