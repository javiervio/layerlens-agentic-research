from tools.fulltext_fetch import parse_manual_links, select_targets


def test_parse_manual_links_skips_comments_and_blanks():
    text = "# header\n\nhttps://arxiv.org/abs/2608.20634v1\nhttps://breken.ai/x\n"
    got = parse_manual_links(text)
    assert len(got) == 2
    assert got[0]["id"] == "2608.20634"          # arxiv id extracted, version stripped
    assert got[1]["source"] == "manual" and got[1]["url"].startswith("https://breken.ai")


def test_select_targets_prioritizes_manual_then_caps():
    manifest = [{"id": f"0000.0000{i}", "link": f"l{i}", "rank": i} for i in range(10)]
    manual = [{"id": "2608.20634", "url": "https://arxiv.org/abs/2608.20634"}]
    sel = select_targets(manifest, manual, cap=3)
    assert sel[0]["id"] == "2608.20634"   # manual first
    assert len(sel) == 3                   # capped
