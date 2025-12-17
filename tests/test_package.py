import pytest
import possessionnet
from possessionnet.pipeline import estimate_possession, PossessionResult

def test_version_exists():
    assert isinstance(possessionnet.__version__, str)
    assert possessionnet.__version__

def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        estimate_possession("definitely-not-a-real-file.mp4")

def test_result_type():
    r = PossessionResult()
    assert hasattr(r, "team_a_seconds")
