from dataclasses import dataclass

@dataclass(frozen=True)
class PossessionResult:
    team_a_seconds: float = 0.0
    team_b_seconds: float = 0.0
    unknown_seconds: float = 0.0

def estimate_possession(video_path: str) -> PossessionResult:
    # TODO: implement detection/tracking
    return PossessionResult()
