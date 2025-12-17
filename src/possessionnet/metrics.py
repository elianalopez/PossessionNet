from __future__ import annotations

from collections import Counter
from typing import Dict

from possessionnet.types import PossessionTimeSeries


def summarize_possession(series: PossessionTimeSeries) -> Dict[str, float]:
    """
    Convert a possession series into fraction-of-time per team.

    Returns a dict with keys:
      - "home"
      - "away"
      - "unknown"

    Notes:
    - Currently, samples are treated as equally weighted.
    - Future versions may weight by sample interval or confidence.
    """
    samples = series.samples
    if not samples:
        return {"home": 0.0, "away": 0.0, "unknown": 0.0}

    counts = Counter(
        (s.team if s.team in {"home", "away"} else "unknown")
        for s in samples
    )

    total = len(samples)
    return {
        "home": counts.get("home", 0) / total,
        "away": counts.get("away", 0) / total,
        "unknown": counts.get("unknown", 0) / total,
    }
