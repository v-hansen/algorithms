import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../sieve-of-eratosthenes')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("sieve_of_eratosthenes", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    sieve_of_eratosthenes = getattr(module, 'sieve_of_eratosthenes')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'sieve_of_eratosthenes'.lower().replace('_', ''):
            sieve_of_eratosthenes = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'sieve_of_eratosthenes' not found in module")

def test_case_1():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_case_2():
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_case_3():
    assert sieve_of_eratosthenes(2) == [2]

