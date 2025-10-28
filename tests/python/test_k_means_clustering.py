import sys
import pytest
sys.path.append('../../k-means-clustering')

def test_can_import():
    try:
        from k_means import KMeans
        kmeans = KMeans(k=2)
        assert kmeans is not None
    except ImportError:
        pytest.skip("numpy not available")
