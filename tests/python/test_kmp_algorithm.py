import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../kmp-algorithm')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("kmp_algorithm", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    kmp_search = getattr(module, 'kmp_search')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'kmp_search'.lower().replace('_', ''):
            kmp_search = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'kmp_search' not found in module")

def test_case_1():
    result = kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
    assert 10 in result

def test_case_2():
    result = kmp_search("AABAACAADAABAABA", "AABA")
    assert 0 in result

