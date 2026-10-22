#!/usr/bin/env python3
"""
Shared agentic-environment relevance vocabulary. One source of truth for the
keyword set used to decide whether a paper or post is on-topic for the research
engine, imported by the arXiv, discovery, and full-text harvesters so they all
judge relevance the same way. Stdlib only.
"""

# Lightweight relevance vocabulary (substring match on lowercased text).
KEYWORDS = [
    "agent", "agentic", "environment", "sandbox", "tool use", "tool-use",
    "tool-calling", "tool calling", "evaluation", "benchmark", "reward hacking",
    "verifier", "verification", "trajectory", "synthetic", "simulation",
    "multi-agent", "multiagent", "orchestration", "mcp", "human-in-the-loop",
    "oversight", "reliability", "reproducib", "world model", "task feasibility",
    "rollout", "self-improve", "optimizer", "llm judge", "llm-as-a-judge",
]


def matched_terms(text):
    """Distinct keyword substrings present in text (lowercased), order preserved."""
    hay = (text or "").lower()
    return [k for k in KEYWORDS if k in hay]


def relevance_score(text):
    """Number of distinct keyword terms matched. 0 means off-topic."""
    return len(matched_terms(text))
