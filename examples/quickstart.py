import sys
from pathlib import Path

from possessionnet.pipeline import estimate_possession

if __name__ == "__main__":
    video_path = sys.argv[1] if len(sys.argv) > 1 else "path/to/video.mp4"

    if not Path(video_path).exists():
        raise SystemExit(
            f"Video not found: {video_path}\n"
            "Usage:\n"
            "  python examples/quickstart.py /path/to/video.mp4"
        )

    result = estimate_possession(video_path)
    print(result)
    print("fps:", result.fps)
    print("frames:", result.frame_count)
    print("duration_seconds:", result.duration_seconds)
