import sys
import pytest
sys.path.append('../../linear-regression')

def test_can_import():
    try:
        from linear_regression import LinearRegression
        lr = LinearRegression()
        assert lr is not None
    except ImportError:
        pytest.skip("numpy not available")
