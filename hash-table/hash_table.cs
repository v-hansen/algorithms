using System;
using System.Collections.Generic;

class HashTable {
    private List<KeyValuePair<string, int>>[] buckets;
    private int size;
    
    public HashTable(int size = 10) {
        this.size = size;
        buckets = new List<KeyValuePair<string, int>>[size];
        for (int i = 0; i < size; i++) {
            buckets[i] = new List<KeyValuePair<string, int>>();
        }
    }
    
    private int Hash(string key) {
        int sum = 0;
        foreach (char c in key) sum += c;
        return sum % size;
    }
    
    public void Put(string key, int value) {
        int index = Hash(key);
        var bucket = buckets[index];
        
        for (int i = 0; i < bucket.Count; i++) {
            if (bucket[i].Key == key) {
                bucket[i] = new KeyValuePair<string, int>(key, value);
                return;
            }
        }
        
        bucket.Add(new KeyValuePair<string, int>(key, value));
    }
    
    public int Get(string key) {
        int index = Hash(key);
        foreach (var pair in buckets[index]) {
            if (pair.Key == key) return pair.Value;
        }
        return -1;
    }
}

class Program {
    static void Main() {
        var ht = new HashTable();
        ht.Put("key1", 100);
        Console.WriteLine(ht.Get("key1"));
    }
}