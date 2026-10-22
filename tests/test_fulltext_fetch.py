from tools.fulltext_fetch import (
    arxiv_id_from, fulltext_urls, html_to_text, fetch_fulltext, render_fulltext_md)


def test_arxiv_id_strips_version_and_parses_urls():
    assert arxiv_id_from("2608.20634v1") == "2608.20634"
    assert arxiv_id_from("2608.20634") == "2608.20634"
    assert arxiv_id_from("https://arxiv.org/html/2608.20634v1") == "2608.20634"
    assert arxiv_id_from("https://ar5iv.labs.arxiv.org/abs/2608.20634") == "2608.20634"
    assert arxiv_id_from("https://breken.ai/post") is None


def test_fulltext_urls_order_ar5iv_html_pdf():
    labels = [lbl for lbl, _ in fulltext_urls("2608.20634")]
    assert labels[0] == "ar5iv" and "pdf" in labels[-1]


def test_html_to_text_strips_markup_and_scripts():
    html = ("<html><head><style>x{}</style></head><body><p>Hello</p>"
            "<script>bad()</script> world</body></html>")
    txt = html_to_text(html)
    assert "Hello" in txt and "world" in txt
    assert "bad()" not in txt and "<p>" not in txt


def test_fetch_fulltext_uses_first_html_source():
    sample = open("tests/fixtures/ar5iv_sample.html", "rb").read()
    got = fetch_fulltext("2608.20634", fetcher=lambda url: sample)
    assert got["source"] == "ar5iv" and "AgentMercury" in got["text"]


def test_fetch_fulltext_falls_back_to_pdf_link_when_html_fails():
    def boom(url):
        raise OSError("blocked")
    got = fetch_fulltext("2608.20634", fetcher=boom)
    assert got["source"] == "pdf-link-only" and got["text"] is None and "pdf" in got["url"]


def test_render_truncates_body():
    # Body char "Q" is chosen so it cannot collide with any header text.
    md = render_fulltext_md(
        {"title": "T", "authors": ["A"], "link": "L", "signal": "upvotes 9"},
        {"source": "ar5iv", "url": "U", "text": "Q" * 100},
        max_chars=10)
    assert "truncated" in md.lower() and md.count("Q") == 10
