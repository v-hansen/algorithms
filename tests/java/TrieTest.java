public class TrieTest {
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("hello");
        trie.insert("world");
        assert trie.search("hello") == true : "Trie search failed";
        assert trie.search("hell") == false : "Trie search failed";
        System.out.println("TrieTest passed");
    }
}
