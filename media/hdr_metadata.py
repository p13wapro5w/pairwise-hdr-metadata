"""第 58 批：同一支 HDR 片子在高亮电视上正常，接到普通电视后高光全糊，字..."""

def max_fall(max_cll, max_fall):
    """返回 MaxFALL。"""
    raise NotImplementedError("TODO: max_fall")

def pq_to_nits(pq):
    """把 PQ 值换算成 nits。"""
    raise NotImplementedError("TODO: pq_to_nits")

def hlg_curve(value):
    """返回 HLG 亮度曲线。"""
    raise NotImplementedError("TODO: hlg_curve")

def sdr_tone_map(nits, max_nits):
    """映射到 SDR。"""
    raise NotImplementedError("TODO: sdr_tone_map")

def subtitle_luma(nits, max_nits):
    """映射字幕亮度。"""
    raise NotImplementedError("TODO: subtitle_luma")

def segment_metadata(segment, default):
    """返回分段元数据。"""
    raise NotImplementedError("TODO: segment_metadata")

def bit_depth(value, bits):
    """按位深量化。"""
    raise NotImplementedError("TODO: bit_depth")

def colorspace_tag(primary):
    """返回色彩空间标记。"""
    raise NotImplementedError("TODO: colorspace_tag")

def thumbnail_map(value, exposure):
    """HDR 缩略图映射。"""
    raise NotImplementedError("TODO: thumbnail_map")

def cache_version(video_id, version):
    """返回元数据缓存键。"""
    raise NotImplementedError("TODO: cache_version")

def dynamic_metadata(frame_values):
    """返回动态元数据首帧。"""
    raise NotImplementedError("TODO: dynamic_metadata")
