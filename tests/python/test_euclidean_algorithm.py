import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../euclidean-algorithm')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("euclidean_algorithm", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    gcd = getattr(module, 'gcd')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'gcd'.lower().replace('_', ''):
            gcd = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'gcd' not found in module")

def test_case_1():
    assert gcd(48, 18) == 6

def test_case_2():
    assert gcd(100, 50) == 50

def test_case_3():
    assert gcd(17, 19) == 1

