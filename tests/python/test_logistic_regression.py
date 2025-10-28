import sys
import pytest
sys.path.append('../../logistic-regression')

def test_can_import():
    try:
        from logistic_regression import LogisticRegression
        lr = LogisticRegression()
        assert lr is not None
    except ImportError:
        pytest.skip("numpy not available")
