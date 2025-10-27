class TrieNode {
    constructor() {
        this.children = new Map();
        this.isEndWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }
    
    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.isEndWord = true;
    }
    
    search(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        return node.isEndWord;
    }
    
    startsWith(prefix) {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        return true;
    }
    
    getAllWordsWithPrefix(prefix) {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return [];
            }
            node = node.children.get(char);
        }
        
        const words = [];
        this._dfs(node, prefix, words);
        return words;
    }
    
    _dfs(node, currentWord, words) {
        if (node.isEndWord) {
            words.push(currentWord);
        }
        
        for (const [char, childNode] of node.children) {
            this._dfs(childNode, currentWord + char, words);
        }
    }
}

// Test
const trie = new Trie();
const words = ["apple", "app", "application", "apply", "banana"];
words.forEach(word => trie.insert(word));

console.log(trie.search("app")); // true
console.log(trie.startsWith("app")); // true
console.log(trie.getAllWordsWithPrefix("app")); // ['app', 'apple', 'application', 'apply']
