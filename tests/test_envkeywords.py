from tools.envkeywords import matched_terms, relevance_score, KEYWORDS


def test_matches_are_distinct_and_lowercased():
    t = "A Multi-Agent sandbox ENVIRONMENT for agentic evaluation"
    terms = matched_terms(t)
    assert "environment" in terms and "sandbox" in terms and "multi-agent" in terms
    assert len(terms) == len(set(terms))


def test_score_counts_distinct_terms():
    assert relevance_score("world model world model") == 1  # one distinct term
    assert relevance_score("no relevant words here") == 0


def test_keywords_cover_core_env_vocab():
    for k in ("agent", "environment", "sandbox", "benchmark", "synthetic"):
        assert k in KEYWORDS
