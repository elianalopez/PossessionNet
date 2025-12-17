import sys

from .pipeline import estimate_possession_series
from .metrics import summarize_possession

def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m teampose /path/to/video.mp4")

    video_path = sys.argv[1]
    series = estimate_possession_series(video_path)
    summary = summarize_possession(series)

    # print metadata and summary
    print("fps:", series.video.fps)
    print("frames:", series.video.frame_count)
    print("duration_seconds:", series.video.duration_seconds)
    print("possession_summary:", summary)

if __name__ == "__main__":
    raise SystemExit(main())
