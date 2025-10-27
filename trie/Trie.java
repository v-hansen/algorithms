import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndWord;
    
    public TrieNode() {
        children = new HashMap<>();
        isEndWord = false;
    }
}

public class Trie {
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return node.isEndWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return true;
    }
    
    public List<String> getAllWordsWithPrefix(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return new ArrayList<>();
            }
            node = node.children.get(c);
        }
        
        List<String> words = new ArrayList<>();
        dfs(node, prefix, words);
        return words;
    }
    
    private void dfs(TrieNode node, String currentWord, List<String> words) {
        if (node.isEndWord) {
            words.add(currentWord);
        }
        
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            dfs(entry.getValue(), currentWord + entry.getKey(), words);
        }
    }
    
    public static void main(String[] args) {
        Trie trie = new Trie();
        String[] words = {"apple", "app", "application", "apply", "banana"};
        
        for (String word : words) {
            trie.insert(word);
        }
        
        System.out.println(trie.search("app")); // true
        System.out.println(trie.startsWith("app")); // true
        System.out.println(trie.getAllWordsWithPrefix("app")); // [app, apple, application, apply]
    }
}
