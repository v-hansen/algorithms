#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;

class HashTable {
    vector<list<pair<string, int>>> buckets;
    int size;
    
    int hash(const string& key) {
        int sum = 0;
        for (char c : key) sum += c;
        return sum % size;
    }
    
public:
    HashTable(int s = 10) : size(s), buckets(s) {}
    
    void put(const string& key, int value) {
        int index = hash(key);
        auto& bucket = buckets[index];
        
        for (auto& pair : bucket) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        bucket.emplace_back(key, value);
    }
    
    int get(const string& key) {
        int index = hash(key);
        for (const auto& pair : buckets[index]) {
            if (pair.first == key) return pair.second;
        }
        return -1;
    }
};

int main() {
    HashTable ht;
    ht.put("key1", 100);
    cout << ht.get("key1") << endl;
    return 0;
}