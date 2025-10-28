import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../edit-distance')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("edit_distance", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    edit_distance = getattr(module, 'edit_distance')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'edit_distance'.lower().replace('_', ''):
            edit_distance = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'edit_distance' not found in module")

def test_case_1():
    assert edit_distance("kitten", "sitting") == 3

def test_case_2():
    assert edit_distance("horse", "ros") == 3

def test_case_3():
    assert edit_distance("", "") == 0

