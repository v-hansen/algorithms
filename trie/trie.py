class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def get_all_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._dfs(node, prefix, words)
        return words
    
    def _dfs(self, node, current_word, words):
        if node.is_end_word:
            words.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, current_word + char, words)

# Test
trie = Trie()
words = ["apple", "app", "application", "apply", "banana"]
for word in words:
    trie.insert(word)

print(trie.search("app"))  # True
print(trie.starts_with("app"))  # True
print(trie.get_all_words_with_prefix("app"))  # ['app', 'apple', 'application', 'apply']
