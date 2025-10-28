import sys
sys.path.append('../../binary-search-tree')
from binary_search_tree import BST

def test_insert_and_search():
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    assert bst.search(30) == True
    assert bst.search(100) == False
