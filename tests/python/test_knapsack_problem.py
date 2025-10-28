import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../knapsack-problem')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("knapsack_problem", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    knapsack_01 = getattr(module, 'knapsack_01')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'knapsack_01'.lower().replace('_', ''):
            knapsack_01 = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'knapsack_01' not found in module")

def test_case_1():
    arr = [10, 20, 30]
    assert knapsack_01(arr, [60, 100, 120], 50) == 220

def test_case_2():
    arr = [1, 1, 1]
    assert knapsack_01(arr, [10, 20, 30], 2) == 50

