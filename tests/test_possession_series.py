import cv2
import numpy as np

from possessionnet.pipeline import estimate_possession_series


def _make_test_video(path, fps=10, frames=20, width=64, height=64):
    """Create a tiny synthetic video for testing."""
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


def test_estimate_possession_series(tmp_path):
    video_path = tmp_path / "test.mp4"
    _make_test_video(video_path)

    series = estimate_possession_series(
        str(video_path),
        sample_every_seconds=1.0,
    )

    # Video metadata is present
    assert series.video.fps > 0
    assert series.video.frame_count > 0
    assert series.video.duration_seconds > 0

    # Time Series samples exist
    assert len(series.samples) > 0

    # First sample starts at t = 0
    assert series.samples[0].t_seconds == 0.0

    # Samples are non-decreasing in time
    times = [s.t_seconds for s in series.samples]
    assert times == sorted(times)

    # Placeholder logic: no team assigned yet
    for sample in series.samples:
        assert sample.team is None
        assert sample.confidence == 0.0
