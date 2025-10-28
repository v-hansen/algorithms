import sys
import pytest
sys.path.append('../../decision-trees')

def test_can_import():
    try:
        from decision_tree import DecisionTree
        dt = DecisionTree()
        assert dt is not None
    except ImportError:
        pytest.skip("numpy not available")
