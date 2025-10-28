import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../longest-common-subsequence')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("longest_common_subsequence", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    lcs_length = getattr(module, 'lcs_length')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'lcs_length'.lower().replace('_', ''):
            lcs_length = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'lcs_length' not found in module")

def test_case_1():
    assert lcs_length("ABCDGH", "AEDFHR") == 3

def test_case_2():
    assert lcs_length("AGGTAB", "GXTXAYB") == 4

