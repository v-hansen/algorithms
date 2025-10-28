import sys
import os
import importlib.util
import glob

# Load algorithm implementation
algo_dir = os.path.join(os.path.dirname(__file__), '../../depth-first-search')
sys.path.insert(0, algo_dir)

# Try different file naming conventions
py_files = glob.glob(os.path.join(algo_dir, '*.py'))
if not py_files:
    raise FileNotFoundError(f"No Python file found in {algo_dir}")

spec = importlib.util.spec_from_file_location("depth_first_search", py_files[0])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Try to get the function
try:
    dfs = getattr(module, 'dfs')
except AttributeError:
    # Try alternative names
    for attr in dir(module):
        if attr.lower().replace('_', '') == 'dfs'.lower().replace('_', ''):
            dfs = getattr(module, attr)
            break
    else:
        raise AttributeError(f"Function 'dfs' not found in module")

def test_case_1():
    graph = {'0': ['1', '2'], '1': ['3'], '2': ['4'], '3': [], '4': []}
    result = dfs(graph, "0")
    assert '0' in result and '1' in result and '2' in result

