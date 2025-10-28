import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../two_pointers')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("two_pointers", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    two_sum = getattr(module, 'two_sum')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'two_sum'.lower().replace('_', ''):
            two_sum = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'two_sum' not found in module")

def test_case_1():
    arr = [2, 7, 11, 15]
    assert two_sum(arr, 9) == [0, 1]

def test_case_2():
    arr = [2, 3, 4]
    assert two_sum(arr, 6) == [0, 2]

