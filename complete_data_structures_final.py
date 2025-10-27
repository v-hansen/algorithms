#!/usr/bin/env python3
import os

def complete_all_data_structures():
    """Completa todas as estruturas de dados"""
    
    # Hash Table - completar todas as linguagens
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/hash-table"
    
    hash_implementations = {
        "hash_table.c": """#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 10

typedef struct Node {
    char* key;
    int value;
    struct Node* next;
} Node;

typedef struct {
    Node* buckets[SIZE];
} HashTable;

int hash(char* key) {
    int sum = 0;
    for (int i = 0; key[i]; i++) sum += key[i];
    return sum % SIZE;
}

void put(HashTable* ht, char* key, int value) {
    int index = hash(key);
    Node* node = malloc(sizeof(Node));
    node->key = strdup(key);
    node->value = value;
    node->next = ht->buckets[index];
    ht->buckets[index] = node;
}

int get(HashTable* ht, char* key) {
    int index = hash(key);
    Node* node = ht->buckets[index];
    while (node) {
        if (strcmp(node->key, key) == 0) return node->value;
        node = node->next;
    }
    return -1;
}

int main() {
    HashTable ht = {0};
    put(&ht, "key1", 100);
    printf("%d\\n", get(&ht, "key1"));
    return 0;
}""",
        
        "hash_table.cpp": """#include <iostream>
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
}""",
        
        "hash_table.go": """package main
import "fmt"

type HashTable struct {
    buckets [][]Pair
    size    int
}

type Pair struct {
    key   string
    value int
}

func NewHashTable(size int) *HashTable {
    return &HashTable{
        buckets: make([][]Pair, size),
        size:    size,
    }
}

func (ht *HashTable) hash(key string) int {
    sum := 0
    for _, c := range key {
        sum += int(c)
    }
    return sum % ht.size
}

func (ht *HashTable) Put(key string, value int) {
    index := ht.hash(key)
    bucket := &ht.buckets[index]
    
    for i, pair := range *bucket {
        if pair.key == key {
            (*bucket)[i].value = value
            return
        }
    }
    *bucket = append(*bucket, Pair{key, value})
}

func (ht *HashTable) Get(key string) int {
    index := ht.hash(key)
    for _, pair := range ht.buckets[index] {
        if pair.key == key {
            return pair.value
        }
    }
    return -1
}

func main() {
    ht := NewHashTable(10)
    ht.Put("key1", 100)
    fmt.Println(ht.Get("key1"))
}""",
        
        "hash_table.php": """<?php
class HashTable {
    private $buckets;
    private $size;
    
    public function __construct($size = 10) {
        $this->size = $size;
        $this->buckets = array_fill(0, $size, []);
    }
    
    private function hash($key) {
        $sum = 0;
        for ($i = 0; $i < strlen($key); $i++) {
            $sum += ord($key[$i]);
        }
        return $sum % $this->size;
    }
    
    public function put($key, $value) {
        $index = $this->hash($key);
        
        foreach ($this->buckets[$index] as &$pair) {
            if ($pair['key'] === $key) {
                $pair['value'] = $value;
                return;
            }
        }
        
        $this->buckets[$index][] = ['key' => $key, 'value' => $value];
    }
    
    public function get($key) {
        $index = $this->hash($key);
        
        foreach ($this->buckets[$index] as $pair) {
            if ($pair['key'] === $key) {
                return $pair['value'];
            }
        }
        
        return null;
    }
}

$ht = new HashTable();
$ht->put("key1", 100);
echo $ht->get("key1");
?>""",
        
        "hash_table.cs": """using System;
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
}"""
    }
    
    for filename, code in hash_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_all_math_algorithms():
    """Completa todos os algoritmos matemáticos"""
    
    # Euclidean Algorithm - completar todas as linguagens
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/euclidean-algorithm"
    
    euclidean_implementations = {
        "euclidean_algorithm.c": """#include <stdio.h>
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    printf("%d\\n", gcd(48, 18));
    return 0;
}""",
        
        "euclidean_algorithm.cpp": """#include <iostream>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    cout << gcd(48, 18) << endl;
    return 0;
}""",
        
        "euclidean_algorithm.go": """package main
import "fmt"

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func main() {
    fmt.Println(gcd(48, 18))
}""",
        
        "euclidean_algorithm.php": """<?php
function gcd($a, $b) {
    while ($b != 0) {
        $temp = $b;
        $b = $a % $b;
        $a = $temp;
    }
    return $a;
}

echo gcd(48, 18);
?>""",
        
        "euclidean_algorithm.cs": """using System;

class EuclideanAlgorithm {
    static int Gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    static void Main() {
        Console.WriteLine(Gcd(48, 18));
    }
}""",
        
        "euclidean_algorithm.rs": """fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a
}

fn main() {
    println!("{}", gcd(48, 18));
}"""
    }
    
    for filename, code in euclidean_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_remaining_algorithms():
    """Completa algoritmos restantes importantes"""
    
    # Two Pointers - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/two_pointers"
    
    two_pointers_implementations = {
        "two_pointers.c": """#include <stdio.h>
int two_sum(int arr[], int n, int target, int result[]) {
    int left = 0, right = n - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            result[0] = left;
            result[1] = right;
            return 1;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return 0;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int result[2];
    if (two_sum(arr, 5, 7, result)) {
        printf("[%d, %d]\\n", result[0], result[1]);
    }
    return 0;
}""",
        
        "two_pointers.cpp": """#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {left, right};
        else if (sum < target) left++;
        else right--;
    }
    return {};
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    auto result = twoSum(arr, 7);
    if (!result.empty()) {
        cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    }
    return 0;
}""",
        
        "two_pointers.go": """package main
import "fmt"

func twoSum(arr []int, target int) []int {
    left, right := 0, len(arr)-1
    for left < right {
        sum := arr[left] + arr[right]
        if sum == target {
            return []int{left, right}
        } else if sum < target {
            left++
        } else {
            right--
        }
    }
    return []int{}
}

func main() {
    arr := []int{1, 2, 3, 4, 5}
    result := twoSum(arr, 7)
    fmt.Println(result)
}""",
        
        "two_pointers.php": """<?php
function twoSum($arr, $target) {
    $left = 0;
    $right = count($arr) - 1;
    
    while ($left < $right) {
        $sum = $arr[$left] + $arr[$right];
        if ($sum == $target) {
            return [$left, $right];
        } elseif ($sum < $target) {
            $left++;
        } else {
            $right--;
        }
    }
    
    return [];
}

$arr = [1, 2, 3, 4, 5];
print_r(twoSum($arr, 7));
?>""",
        
        "two_pointers.cs": """using System;

class TwoPointers {
    static int[] TwoSum(int[] arr, int target) {
        int left = 0, right = arr.Length - 1;
        
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return new int[] {left, right};
            else if (sum < target) left++;
            else right--;
        }
        
        return new int[] {};
    }
    
    static void Main() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = TwoSum(arr, 7);
        if (result.Length > 0) {
            Console.WriteLine($"[{result[0]}, {result[1]}]");
        }
    }
}"""
    }
    
    for filename, code in two_pointers_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando estruturas de dados e algoritmos matemáticos...")
    complete_all_data_structures()
    complete_all_math_algorithms()
    complete_remaining_algorithms()
    print("Segunda fase de completamento finalizada!")
