from possessionnet.pipeline import estimate_possession

if __name__ == "__main__":
    # Replace with a real path later
    result = estimate_possession("path/to/video.mp4")
    print(result)
    print("fps:", result.fps)
    print("frames:", result.frame_count)
    print("duration_seconds:", result.duration_seconds)
