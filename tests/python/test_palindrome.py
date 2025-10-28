import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../palindrome')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("palindrome", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    is_palindrome_simple = getattr(module, 'is_palindrome_simple')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'is_palindrome_simple'.lower().replace('_', ''):
            is_palindrome_simple = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'is_palindrome_simple' not found in module")

def test_case_1():
    assert is_palindrome_simple("racecar") == True

def test_case_2():
    assert is_palindrome_simple("hello") == False

def test_case_3():
    assert is_palindrome_simple("") == True

