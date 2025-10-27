#!/usr/bin/env python3
import os

def complete_remaining_small_files():
    """Completa todos os arquivos pequenos restantes"""
    
    # BFS - JavaScript e TypeScript
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/breadth-first-search"
    
    with open(f"{base_dir}/breadth_first_search.js", "w") as f:
        f.write("""function bfs(graph, start) {
    const visited = new Set();
    const queue = [start];
    visited.add(start);
    
    while (queue.length > 0) {
        const node = queue.shift();
        process.stdout.write(node + " ");
        
        const neighbors = graph[node] || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
}

const graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]};
bfs(graph, 2);""")

    with open(f"{base_dir}/breadth_first_search.ts", "w") as f:
        f.write("""function bfs(graph: {[key: number]: number[]}, start: number): void {
    const visited = new Set<number>();
    const queue: number[] = [start];
    visited.add(start);
    
    while (queue.length > 0) {
        const node = queue.shift()!;
        process.stdout.write(node + " ");
        
        const neighbors = graph[node] || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
}

const graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]};
bfs(graph, 2);""")

    # Quick Sort - C
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/quick-sort"
    
    with open(f"{base_dir}/quick_sort.c", "w") as f:
        f.write("""#include <stdio.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);
    quickSort(arr, 0, n - 1);
    
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\\n");
    
    return 0;
}""")

    # Edit Distance - pequenos arquivos
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/edit-distance"
    
    with open(f"{base_dir}/edit_distance.c", "w") as f:
        f.write("""#include <stdio.h>
#include <string.h>

int min(int a, int b, int c) {
    int min_ab = a < b ? a : b;
    return min_ab < c ? min_ab : c;
}

int editDistance(char* str1, char* str2) {
    int m = strlen(str1), n = strlen(str2);
    int dp[m + 1][n + 1];
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
            }
        }
    }
    
    return dp[m][n];
}

int main() {
    printf("%d\\n", editDistance("kitten", "sitting"));
    return 0;
}""")

    with open(f"{base_dir}/edit_distance.go", "w") as f:
        f.write("""package main
import "fmt"

func min(a, b, c int) int {
    if a < b && a < c {
        return a
    } else if b < c {
        return b
    }
    return c
}

func editDistance(str1, str2 string) int {
    m, n := len(str1), len(str2)
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }
    
    for i := 0; i <= m; i++ {
        dp[i][0] = i
    }
    for j := 0; j <= n; j++ {
        dp[0][j] = j
    }
    
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if str1[i-1] == str2[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            }
        }
    }
    
    return dp[m][n]
}

func main() {
    fmt.Println(editDistance("kitten", "sitting"))
}""")

    with open(f"{base_dir}/edit_distance.clj", "w") as f:
        f.write("""(defn edit-distance [str1 str2]
  (let [m (count str1)
        n (count str2)
        dp (vec (for [i (range (inc m))]
                 (vec (repeat (inc n) 0))))]
    
    (let [dp (reduce (fn [dp i] (assoc-in dp [i 0] i)) dp (range (inc m)))
          dp (reduce (fn [dp j] (assoc-in dp [0 j] j)) dp (range (inc n)))]
      
      (loop [dp dp i 1]
        (if (> i m)
          (get-in dp [m n])
          (recur
            (loop [dp dp j 1]
              (if (> j n)
                dp
                (recur
                  (if (= (nth str1 (dec i)) (nth str2 (dec j)))
                    (assoc-in dp [i j] (get-in dp [(dec i) (dec j)]))
                    (assoc-in dp [i j] (inc (min (get-in dp [(dec i) j])
                                                (get-in dp [i (dec j)])
                                                (get-in dp [(dec i) (dec j)])))))
                  (inc j))))
            (inc i)))))))

(println (edit-distance "kitten" "sitting"))""")

    with open(f"{base_dir}/edit_distance.php", "w") as f:
        f.write("""<?php
function editDistance($str1, $str2) {
    $m = strlen($str1);
    $n = strlen($str2);
    $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    
    for ($i = 0; $i <= $m; $i++) $dp[$i][0] = $i;
    for ($j = 0; $j <= $n; $j++) $dp[0][$j] = $j;
    
    for ($i = 1; $i <= $m; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            if ($str1[$i-1] == $str2[$j-1]) {
                $dp[$i][$j] = $dp[$i-1][$j-1];
            } else {
                $dp[$i][$j] = 1 + min($dp[$i-1][$j], $dp[$i][$j-1], $dp[$i-1][$j-1]);
            }
        }
    }
    
    return $dp[$m][$n];
}

echo editDistance("kitten", "sitting");
?>""")

def complete_remaining_algorithms():
    """Completa algoritmos restantes"""
    
    # Euclidean Algorithm - pequenos
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/euclidean-algorithm"
    
    with open(f"{base_dir}/euclidean_algorithm.clj", "w") as f:
        f.write("""(defn gcd [a b]
  (if (zero? b) a (recur b (mod a b))))

(defn lcm [a b]
  (/ (* a b) (gcd a b)))

(defn extended-gcd [a b]
  (if (zero? b)
    [a 1 0]
    (let [[g x1 y1] (extended-gcd b (mod a b))
          x (- y1 (* (quot a b) x1))
          y x1]
      [g x y])))

(println "GCD:" (gcd 48 18))
(println "LCM:" (lcm 48 18))
(println "Extended GCD:" (extended-gcd 48 18))""")

    with open(f"{base_dir}/euclidean_algorithm.rb", "w") as f:
        f.write("""def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

def lcm(a, b)
  (a * b) / gcd(a, b)
end

def extended_gcd(a, b)
  return [a, 1, 0] if b == 0
  
  g, x1, y1 = extended_gcd(b, a % b)
  x = y1
  y = x1 - (a / b) * y1
  
  [g, x, y]
end

puts "GCD: #{gcd(48, 18)}"
puts "LCM: #{lcm(48, 18)}"
puts "Extended GCD: #{extended_gcd(48, 18)}"""")

    # Completar outros pequenos
    complete_small_files()

def complete_small_files():
    """Completa arquivos muito pequenos restantes"""
    
    # KMP Algorithm - PHP
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/kmp-algorithm"
    
    with open(f"{base_dir}/kmp_algorithm.php", "w") as f:
        f.write("""<?php
function computeLPS($pattern) {
    $m = strlen($pattern);
    $lps = array_fill(0, $m, 0);
    $len = 0;
    $i = 1;
    
    while ($i < $m) {
        if ($pattern[$i] == $pattern[$len]) {
            $len++;
            $lps[$i] = $len;
            $i++;
        } else {
            if ($len != 0) {
                $len = $lps[$len - 1];
            } else {
                $lps[$i] = 0;
                $i++;
            }
        }
    }
    
    return $lps;
}

function KMPSearch($text, $pattern) {
    $n = strlen($text);
    $m = strlen($pattern);
    $lps = computeLPS($pattern);
    
    $i = 0; // index for text
    $j = 0; // index for pattern
    $matches = [];
    
    while ($i < $n) {
        if ($pattern[$j] == $text[$i]) {
            $i++;
            $j++;
        }
        
        if ($j == $m) {
            $matches[] = $i - $j;
            $j = $lps[$j - 1];
        } elseif ($i < $n && $pattern[$j] != $text[$i]) {
            if ($j != 0) {
                $j = $lps[$j - 1];
            } else {
                $i++;
            }
        }
    }
    
    return $matches;
}

$text = "ABABDABACDABABCABCABCABCABC";
$pattern = "ABABCABCABCABC";
$matches = KMPSearch($text, $pattern);
print_r($matches);
?>""")

    # Trie - C e PHP
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/trie"
    
    with open(f"{base_dir}/trie.c", "w") as f:
        f.write("""#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define ALPHABET_SIZE 26

typedef struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    bool isEndOfWord;
} TrieNode;

TrieNode* createNode() {
    TrieNode* node = malloc(sizeof(TrieNode));
    node->isEndOfWord = false;
    for (int i = 0; i < ALPHABET_SIZE; i++)
        node->children[i] = NULL;
    return node;
}

void insert(TrieNode* root, char* word) {
    TrieNode* current = root;
    for (int i = 0; word[i]; i++) {
        int index = word[i] - 'a';
        if (!current->children[index])
            current->children[index] = createNode();
        current = current->children[index];
    }
    current->isEndOfWord = true;
}

bool search(TrieNode* root, char* word) {
    TrieNode* current = root;
    for (int i = 0; word[i]; i++) {
        int index = word[i] - 'a';
        if (!current->children[index])
            return false;
        current = current->children[index];
    }
    return current && current->isEndOfWord;
}

int main() {
    TrieNode* root = createNode();
    insert(root, "hello");
    printf("%s\\n", search(root, "hello") ? "Found" : "Not found");
    return 0;
}""")

    with open(f"{base_dir}/trie.php", "w") as f:
        f.write("""<?php
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
?>""")

if __name__ == "__main__":
    print("Completando fase final...")
    complete_remaining_small_files()
    complete_remaining_algorithms()
    print("Fase final completada!")
