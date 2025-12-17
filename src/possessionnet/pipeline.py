from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import cv2

@dataclass(frozen=True)
class PossessionResult:
    team_a_seconds: float = 0.0
    team_b_seconds: float = 0.0
    unknown_seconds: float = 0.0

    # video metadata (real now)
    fps: float = 0.0
    frame_count: int = 0
    duration_seconds: float = 0.0


def estimate_possession(video_path: str) -> PossessionResult:
    """
    Load a video and return basic metadata + placeholder possession stats.

    Future versions will detect teams/ball and compute team_a_seconds/team_b_seconds.
    """
    p = Path(video_path)
    if not p.exists():
        raise FileNotFoundError(f"Video not found: {p}")
    if not p.is_file():
        raise ValueError(f"Not a file: {p}")

    cap = cv2.VideoCapture(str(p))
    if not cap.isOpened():
        raise ValueError(f"Failed to open video: {p}")

    fps = float(cap.get(cv2.CAP_PROP_FPS) or 0.0)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)

    cap.release()

    duration_seconds = (frame_count / fps) if (fps > 0 and frame_count > 0) else 0.0

    return PossessionResult(
        team_a_seconds=0.0,
        team_b_seconds=0.0,
        unknown_seconds=duration_seconds,  # everything unknown for now
        fps=fps,
        frame_count=frame_count,
        duration_seconds=duration_seconds,
    )
