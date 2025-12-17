# PossessionNet

PossessionNet is a computer vision toolkit for estimating **team possession** of an object from video. Current functionality focuses on loading a video and returning basic video metadata (fps, frame count, duration) as a foundation for future possession estimation.

## Project Status

This project is in early development (`v0.2.0`).

Lastest updates include adding placeholder logic for possession estimates to demonstrate end-to-end data flow (video ⟶ video series ⟶ video summary).

Current possession logic is expected to be 100% "unknown" until labeling logic is added. 

# Install

Editable install for development:

```
pip install -e 
```

## Usage


### CLI 
Run the module CLI:

```
python -m possessionnet /path/to/video.mp4
```

#### Current Output

```
fps: 29.97
frames: 6536
duration_seconds: 218.084
possession_summary: {'home': 0.0, 'away': 0.0, 'unknown': 1.0}
```

## quickstart

Run the quickstart example:

```
python examples/quickstart.py /path/to/video.mp4
```

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