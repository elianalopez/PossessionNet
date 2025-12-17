import cv2
import numpy as np

from possessionnet.metrics import summarize_possession
from possessionnet.pipeline import estimate_possession_series
from possessionnet.types import VideoMetadata, PossessionTimeSeries


def _make_test_video(path, fps=10, frames=20, width=64, height=64):
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(path), fourcc, fps, (width, height))
    for i in range(frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        cv2.putText(
            frame,
            str(i),
            (5, height // 2),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (255, 255, 255),
            1,
        )
        writer.write(frame)
    writer.release()


def test_summarize_possession_all_unknown(tmp_path):
    video_path = tmp_path / "test.mp4"
    _make_test_video(video_path)

    series = estimate_possession_series(str(video_path), sample_every_seconds=1.0)
    summary = summarize_possession(series)

    assert set(summary.keys()) == {"home", "away", "unknown"}
    assert summary["home"] == 0.0
    assert summary["away"] == 0.0
    assert summary["unknown"] == 1.0


def test_summarize_possession_empty_samples():
    # Import types here so this test doesn't depend on video/OpenCV.

    series = PossessionTimeSeries(
        video=VideoMetadata(fps=30.0, frame_count=0, duration_seconds=0.0),
        samples=[],
    )

    summary = summarize_possession(series)
    assert summary == {"home": 0.0, "away": 0.0, "unknown": 0.0}
