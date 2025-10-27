class TrieNode {
    children: Map<string, TrieNode> = new Map();
    isEnd: boolean = false;
}

class Trie {
    private root = new TrieNode();
    
    insert(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isEnd = true;
    }
    
    search(word: string): boolean {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) return false;
            node = node.children.get(char)!;
        }
        return node.isEnd;
    }
}

const trie = new Trie();
trie.insert("hello");
console.log(trie.search("hello"));