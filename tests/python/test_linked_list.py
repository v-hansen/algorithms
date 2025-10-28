import sys
sys.path.append('../../linked-list')
from linked_list import LinkedList

def test_append_and_display():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.display() == [1, 2, 3]
