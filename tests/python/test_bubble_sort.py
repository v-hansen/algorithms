import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../bubble-sort')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("bubble_sort", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    bubble_sort = getattr(module, 'bubble_sort')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'bubble_sort'.lower().replace('_', ''):
            bubble_sort = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'bubble_sort' not found in module")

def test_case_1():
    arr = [5, 4, 3, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]

def test_case_2():
    arr = [1, 2, 3]
    assert bubble_sort(arr) == [1, 2, 3]

