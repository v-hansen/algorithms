<?php
class TrieNode {
    public $children = [];
    public $isEndOfWord = false;
}

class Trie {
    private $root;
    
    public function __construct() {
        $this->root = new TrieNode();
    }
    
    public function insert($word) {
        $current = $this->root;
        
        for ($i = 0; $i < strlen($word); $i++) {
            $char = $word[$i];
            if (!isset($current->children[$char])) {
                $current->children[$char] = new TrieNode();
            }
            $current = $current->children[$char];
        }
        
        $current->isEndOfWord = true;
    }
    
    public function search($word) {
        $current = $this->root;
        
        for ($i = 0; $i < strlen($word); $i++) {
            $char = $word[$i];
            if (!isset($current->children[$char])) {
                return false;
            }
            $current = $current->children[$char];
        }
        
        return $current->isEndOfWord;
    }
}

$trie = new Trie();
$trie->insert("hello");
echo $trie->search("hello") ? "Found" : "Not found";
?>
