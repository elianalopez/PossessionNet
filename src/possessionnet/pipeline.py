from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class PossessionResult:
    team_a_seconds: float = 0.0
    team_b_seconds: float = 0.0
    unknown_seconds: float = 0.0

def estimate_possession(video_path: str) -> PossessionResult:
    p = Path(video_path)
    if not p.exists():
        raise FileNotFoundError(f"Video not found: {p}")
    if not p.is_file():
        raise ValueError(f"Not a file: {p}")

    # TODO: implement detection/tracking
    return PossessionResult()
