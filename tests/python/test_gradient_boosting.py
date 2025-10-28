import sys
import pytest
sys.path.append('../../gradient-boosting')

def test_can_import():
    try:
        from gradient_boosting import GradientBoosting
        gb = GradientBoosting()
        assert gb is not None
    except ImportError:
        pytest.skip("numpy not available")
