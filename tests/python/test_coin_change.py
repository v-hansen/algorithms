import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../coin-change')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("coin_change", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    coin_change = getattr(module, 'coin_change')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'coin_change'.lower().replace('_', ''):
            coin_change = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'coin_change' not found in module")

def test_case_1():
    arr = [1, 2, 5]
    assert coin_change(arr, 11) == 3

def test_case_2():
    arr = [2]
    assert coin_change(arr, 3) == -1

def test_case_3():
    arr = [1]
    assert coin_change(arr, 0) == 0

