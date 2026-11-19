import pytest
from media import hdr_metadata as mod

CASES = [
    ("fall", 'm.max_fall(1000, 500) == 500'),
    ("pq_zero", 'm.pq_to_nits(0.0) == approx(0.0)'),
    ("pq_one", 'm.pq_to_nits(1.0) == approx(10000.0)'),
    ("hlg", 'm.hlg_curve(0.25) == approx(0.5)'),
    ("sdr_clamp", 'm.sdr_tone_map(2000, 1000) == approx(1.0)'),
    ("sdr_half", 'm.sdr_tone_map(500, 1000) == approx(0.5)'),
    ("subtitle", 'm.subtitle_luma(2000, 1000) == approx(1.0)'),
    ("segment_default", 'm.segment_metadata(None, {"a": 1}) == {"a": 1}'),
    ("segment_value", 'm.segment_metadata({"a": 2}, {"a": 1}) == {"a": 2}'),
    ("bit", 'm.bit_depth(0.5, 10) == approx(0.4995, rel=1e-3)'),
    ("colorspace", 'm.colorspace_tag("BT.2020") == "bt.2020"'),
    ("thumb", 'm.thumbnail_map(2.0, 0.5) == approx(1.0)'),
    ("cache", 'm.cache_version("v1", "r2") == "v1#r2"'),
    ("dynamic", 'm.dynamic_metadata([100, 200]) == 100'),
    ("dynamic_empty", 'm.dynamic_metadata([]) == 0')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
