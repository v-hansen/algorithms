import sys
import os
import importlib.util

# Load hash_table.py
hash_table_dir = os.path.join(os.path.dirname(__file__), '../../hash-table')
spec = importlib.util.spec_from_file_location("hash_table", 
    os.path.join(hash_table_dir, "hash_table.py"))
hash_table_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hash_table_module)
HashTable = hash_table_module.HashTable

def test_insert_and_get():
    ht = HashTable()
    ht.put("key1", "value1")
    assert ht.get("key1") == "value1"

def test_update_value():
    ht = HashTable()
    ht.put("key1", "value1")
    ht.put("key1", "value2")
    assert ht.get("key1") == "value2"

def test_get_nonexistent():
    import pytest
    ht = HashTable()
    with pytest.raises(KeyError):
        ht.get("nonexistent")

def test_multiple_keys():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3
