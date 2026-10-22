import json

from tools.discovery_harvest import (
    hf_candidates, openalex_candidates, rank_candidates, render_discovery_md)


def test_hf_keeps_only_env_relevant_with_upvotes():
    data = json.load(open("tests/fixtures/hf_daily.json"))
    cs = hf_candidates(data)
    assert all(c["source"] == "hf-daily" and c["signal_kind"] == "upvotes" for c in cs)
    assert all(c["signal"] >= 0 for c in cs)
    # The protein-folding paper is off-topic and must be dropped.
    assert all("protein" not in (c["title"] + c["summary"]).lower() for c in cs)
    assert any("environment" in (c["title"] + c["summary"]).lower()
               or "agent" in (c["title"] + c["summary"]).lower() for c in cs)


def test_openalex_maps_citations():
    data = json.load(open("tests/fixtures/openalex.json"))
    cs = openalex_candidates(data)
    assert cs, "expected at least one env-relevant OpenAlex candidate"
    assert all(c["signal_kind"] == "citations" for c in cs)
    assert any(c["signal"] == 12 for c in cs)


def test_rank_dedupes_by_id_and_sorts():
    a = {"id": "2608.20634", "title": "Agent env", "summary": "sandbox", "link": "x",
         "signal_kind": "upvotes", "signal": 2, "source": "hf-daily"}
    b = {"id": "2608.20634", "title": "Agent env", "summary": "sandbox", "link": "x",
         "signal_kind": "citations", "signal": 9, "source": "openalex"}
    c = {"id": "1111.00001", "title": "agent", "summary": "benchmark", "link": "y",
         "signal_kind": "recency", "signal": 0, "source": "arxiv"}
    ranked = rank_candidates([a, b, c])
    assert len([r for r in ranked if r["id"] == "2608.20634"]) == 1  # deduped
    assert ranked[0]["id"] in {"2608.20634", "1111.00001"}           # sorted


def test_render_handles_zero_candidates():
    md = render_discovery_md([], "2026-W43", "2026-10-22")
    assert "no candidates" in md.lower()
