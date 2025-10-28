import sys
import pytest
sys.path.append('../../k-nearest-neighbors')

def test_can_import():
    try:
        from knn import KNN
        knn = KNN(k=3)
        assert knn is not None
    except ImportError:
        pytest.skip("numpy not available")
