import sys
import os

# Add the binary-search directory to path
binary_search_dir = os.path.join(os.path.dirname(__file__), '../../binary-search')
sys.path.insert(0, binary_search_dir)

# Import by loading the file directly
import importlib.util
spec = importlib.util.spec_from_file_location("binary_search", 
    os.path.join(binary_search_dir, "binary-search.py"))
binary_search_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(binary_search_module)
binary_search = binary_search_module.binary_search

def test_found_middle():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2

def test_found_first():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0

def test_found_last():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4

def test_not_found():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

def test_empty_array():
    assert binary_search([], 1) == -1

def test_single_element_found():
    assert binary_search([5], 5) == 0

def test_single_element_not_found():
    assert binary_search([5], 3) == -1
