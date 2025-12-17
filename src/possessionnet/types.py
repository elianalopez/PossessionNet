from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class VideoMetadata:
    fps: float
    frame_count: int
    duration_seconds: float


@dataclass(frozen=True)
class PossessionSample:
    t_seconds: float
    team: Optional[str]  # "home" | "away" | None (unknown)
    confidence: float    # 0..1


@dataclass(frozen=True)
class PossessionTimeSeries:
    video: VideoMetadata
    samples: List[PossessionSample]
