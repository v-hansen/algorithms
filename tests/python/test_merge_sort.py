import sys
import os
import importlib.util

# Load merge_sort.py
merge_sort_dir = os.path.join(os.path.dirname(__file__), '../../merge-sort')
spec = importlib.util.spec_from_file_location("merge_sort", 
    os.path.join(merge_sort_dir, "merge_sort.py"))
merge_sort_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(merge_sort_module)
merge_sort = merge_sort_module.merge_sort

def test_already_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_random_order():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_empty_array():
    assert merge_sort([]) == []

def test_single_element():
    assert merge_sort([42]) == [42]

def test_duplicates():
    assert merge_sort([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]

def test_negative_numbers():
    assert merge_sort([-3, -1, -5, 0, 2]) == [-5, -3, -1, 0, 2]
