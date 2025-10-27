class TrieNode {
    val children = mutableMapOf<Char, TrieNode>()
    var isEnd = false
}

class Trie {
    private val root = TrieNode()
    
    fun insert(word: String) {
        var node = root
        for (char in word) {
            node = node.children.getOrPut(char) { TrieNode() }
        }
        node.isEnd = true
    }
    
    fun search(word: String): Boolean {
        var node = root
        for (char in word) {
            node = node.children[char] ?: return false
        }
        return node.isEnd
    }
    
    fun startsWith(prefix: String): Boolean {
        var node = root
        for (char in prefix) {
            node = node.children[char] ?: return false
        }
        return true
    }
}

fun main() {
    val trie = Trie()
    trie.insert("hello")
    trie.insert("world")
    println("Search 'hello': ${trie.search("hello")}")
    println("Starts with 'hel': ${trie.startsWith("hel")}")
}
