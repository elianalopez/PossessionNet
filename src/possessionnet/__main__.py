import sys
from .pipeline import estimate_possession

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m possessionnet <video_path>")
        return 2

    result = estimate_possession(sys.argv[1])
    print(result)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
