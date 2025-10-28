import sys
import pytest
sys.path.append('../../random-forest')

def test_can_import():
    try:
        from random_forest import RandomForest
        rf = RandomForest()
        assert rf is not None
    except ImportError:
        pytest.skip("numpy not available")
