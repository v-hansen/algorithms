import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../dynamic-programming')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("dynamic_programming", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    fibonacci_dp = getattr(module, 'fibonacci_dp')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'fibonacci_dp'.lower().replace('_', ''):
            fibonacci_dp = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'fibonacci_dp' not found in module")

def test_case_1():
    assert fibonacci_dp(10) == 55

def test_case_2():
    assert fibonacci_dp(5) == 5

