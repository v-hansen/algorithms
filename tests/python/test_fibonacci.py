import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../fibonacci')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("fibonacci", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    fibonacci_iterative = getattr(module, 'fibonacci_iterative')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'fibonacci_iterative'.lower().replace('_', ''):
            fibonacci_iterative = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'fibonacci_iterative' not found in module")

def test_case_1():
    assert fibonacci_iterative(0) == 0

def test_case_2():
    assert fibonacci_iterative(1) == 1

def test_case_3():
    assert fibonacci_iterative(5) == 5

def test_case_4():
    assert fibonacci_iterative(10) == 55

