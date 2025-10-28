import sys
sys.path.append('../../trie')
from trie import Trie

def test_insert_and_search():
    trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    assert trie.search("hello") == True
    assert trie.search("hell") == False
