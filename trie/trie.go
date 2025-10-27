package main

import "fmt"

type TrieNode struct {
    children  map[rune]*TrieNode
    isEndWord bool
}

type Trie struct {
    root *TrieNode
}

func NewTrie() *Trie {
    return &Trie{
        root: &TrieNode{
            children:  make(map[rune]*TrieNode),
            isEndWord: false,
        },
    }
}

func (t *Trie) Insert(word string) {
    node := t.root
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            node.children[char] = &TrieNode{
                children:  make(map[rune]*TrieNode),
                isEndWord: false,
            }
        }
        node = node.children[char]
    }
    node.isEndWord = true
}

func (t *Trie) Search(word string) bool {
    node := t.root
    for _, char := range word {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return node.isEndWord
}

func (t *Trie) StartsWith(prefix string) bool {
    node := t.root
    for _, char := range prefix {
        if _, exists := node.children[char]; !exists {
            return false
        }
        node = node.children[char]
    }
    return true
}

func main() {
    trie := NewTrie()
    words := []string{"apple", "app", "application", "apply", "banana"}
    
    for _, word := range words {
        trie.Insert(word)
    }
    
    fmt.Printf("Search 'app': %t\n", trie.Search("app"))
    fmt.Printf("Starts with 'app': %t\n", trie.StartsWith("app"))
}
