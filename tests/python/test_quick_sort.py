import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../quick-sort')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("quick_sort", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    quick_sort = getattr(module, 'quick_sort')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'quick_sort'.lower().replace('_', ''):
            quick_sort = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'quick_sort' not found in module")

def test_case_1():
    arr = [5, 4, 3, 2, 1]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

def test_case_2():
    arr = [3, 1, 4, 1, 5]
    assert quick_sort(arr) == [1, 1, 3, 4, 5]

