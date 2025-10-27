class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if not node:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        return node
    
    def search(self, data):
        return self._search(self.root, data)
    
    def _search(self, node, data):
        if not node or node.data == data:
            return node is not None
        
        if data < node.data:
            return self._search(node.left, data)
        return self._search(node.right, data)

# Test
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
print(bst.search(30))  # True
