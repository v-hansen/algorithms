import sys
import pytest
sys.path.append('../../support-vector-machines')

def test_can_import():
    try:
        from svm import SVM
        svm = SVM()
        assert svm is not None
    except ImportError:
        pytest.skip("numpy not available")
