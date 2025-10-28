import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../matrix-multiplication')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("matrix_multiplication", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    matrix_multiply = getattr(module, 'matrix_multiply')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'matrix_multiply'.lower().replace('_', ''):
            matrix_multiply = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'matrix_multiply' not found in module")

def test_case_1():
    arr = [[1, 2], [3, 4]]
    assert matrix_multiply(arr, [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]

