import numpy as np
import cv2

from possessionnet.pipeline import estimate_possession

def _write_tiny_video(path: str, fps: float = 30.0, frames: int = 30) -> None:
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(path, fourcc, fps, (64, 64))
    for _ in range(frames):
        frame = np.zeros((64, 64, 3), dtype=np.uint8)
        out.write(frame)
    out.release()

def test_estimate_possession_reads_metadata(tmp_path):
    video_path = tmp_path / "tiny.mp4"
    _write_tiny_video(str(video_path))

    r = estimate_possession(str(video_path))
    assert r.fps > 0
    assert r.frame_count > 0
    assert r.duration_seconds > 0
