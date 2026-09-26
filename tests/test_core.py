from paper_screener_core import score_abstract, rank_papers, keyword_hits

def test_hits():
    h = keyword_hits("quantum quantum finance", ["quantum", "finance"])
    assert h["quantum"] == 2

def test_rank():
    papers = [{"title": "A", "abstract": "quantum trading"}, {"title": "B", "abstract": "cats"}]
    r = rank_papers(papers, ["quantum"])
    assert r[0]["title"] == "A"
