# PossessionNet

PossessionNet is a computer vision toolkit for estimating **team possession** of an object from video.Current functionality focuses on loading a video and returning basic video metadata (fps, frame count, duration) as a foundation for future possession estimation.

## Project Status

This project is in early development (`v0.1.0`).
Current functionality is limited to video loading and metadata extraction.

APIs may change as features are added.

# Install

Editable install for development:

```
pip install -e 
```

## Usage

Run the module CLI:

```
python -m possessionnet /path/to/video.mp4
```

Or run the quickstart example:

```
python examples/quickstart.py /path/to/video.mp4
```

## Current Output

At this stage, the pipeline returns video metadata such as:

- fps
- frame_count
- duration_seconds

This provides a stable base for future work such as player tracking, ball
detection, team classification, and possession estimation.

## Development

Run tests:

```
pytest -q
```

Lint:

```
ruff check
```

## License

MIT