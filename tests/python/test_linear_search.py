import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../linear-search')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("linear_search", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    linear_search = getattr(module, 'linear_search')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'linear_search'.lower().replace('_', ''):
            linear_search = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'linear_search' not found in module")

def test_case_1():
    arr = [['3, 1, 4, 1, 5']]
    assert linear_search(arr, 4) == 2

def test_case_2():
    arr = [['3, 1, 4, 1, 5']]
    assert linear_search(arr, 9) == -1

def test_case_3():
    arr = [[]]
    assert linear_search(arr, 1) == -1

