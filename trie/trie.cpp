#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndWord;
    
    TrieNode() : isEndWord(false) {}
};

class Trie {
private:
    TrieNode* root;
    
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndWord = true;
    }
    
    bool search(const string& word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndWord;
    }
    
    bool startsWith(const string& prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
};

int main() {
    Trie trie;
    vector<string> words = {"apple", "app", "application", "apply", "banana"};
    
    for (const string& word : words) {
        trie.insert(word);
    }
    
    cout << "Search 'app': " << trie.search("app") << endl;
    cout << "Starts with 'app': " << trie.startsWith("app") << endl;
    
    return 0;
}
