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

    # Euclidean Algorithm - Ruby
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/euclidean-algorithm"
    
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
puts "Extended GCD: #{extended_gcd(48, 18)}" """)

def complete_longest_common_subsequence():
    """Completa LCS implementações pequenas"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/longest-common-subsequence"
    
    # C
    with open(f"{base_dir}/longest_common_subsequence.c", "w") as f:
        f.write("""#include <stdio.h>
#include <string.h>

int max(int a, int b) { return a > b ? a : b; }

int lcs(char* X, char* Y) {
    int m = strlen(X), n = strlen(Y);
    int L[m+1][n+1];
    
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i-1] == Y[j-1])
                L[i][j] = L[i-1][j-1] + 1;
            else
                L[i][j] = max(L[i-1][j], L[i][j-1]);
        }
    }
    
    return L[m][n];
}

int main() {
    printf("%d\\n", lcs("ABCDGH", "AEDFHR"));
    return 0;
}""")

    # Go
    with open(f"{base_dir}/longest_common_subsequence.go", "w") as f:
        f.write("""package main
import "fmt"

func max(a, b int) int {
    if a > b { return a }
    return b
}

func lcs(X, Y string) int {
    m, n := len(X), len(Y)
    L := make([][]int, m+1)
    for i := range L {
        L[i] = make([]int, n+1)
    }
    
    for i := 0; i <= m; i++ {
        for j := 0; j <= n; j++ {
            if i == 0 || j == 0 {
                L[i][j] = 0
            } else if X[i-1] == Y[j-1] {
                L[i][j] = L[i-1][j-1] + 1
            } else {
                L[i][j] = max(L[i-1][j], L[i][j-1])
            }
        }
    }
    
    return L[m][n]
}

func main() {
    fmt.Println(lcs("ABCDGH", "AEDFHR"))
}""")

    # Kotlin
    with open(f"{base_dir}/UlongestUcommonUsubsequence.kt", "w") as f:
        f.write("""fun lcs(X: String, Y: String): Int {
    val m = X.length
    val n = Y.length
    val L = Array(m + 1) { IntArray(n + 1) }
    
    for (i in 0..m) {
        for (j in 0..n) {
            when {
                i == 0 || j == 0 -> L[i][j] = 0
                X[i-1] == Y[j-1] -> L[i][j] = L[i-1][j-1] + 1
                else -> L[i][j] = maxOf(L[i-1][j], L[i][j-1])
            }
        }
    }
    
    return L[m][n]
}

fun main() {
    println(lcs("ABCDGH", "AEDFHR"))
}""")

    # PHP
    with open(f"{base_dir}/lcs.php", "w") as f:
        f.write("""<?php
function lcs($X, $Y) {
    $m = strlen($X);
    $n = strlen($Y);
    $L = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    
    for ($i = 0; $i <= $m; $i++) {
        for ($j = 0; $j <= $n; $j++) {
            if ($i == 0 || $j == 0) {
                $L[$i][$j] = 0;
            } elseif ($X[$i-1] == $Y[$j-1]) {
                $L[$i][$j] = $L[$i-1][$j-1] + 1;
            } else {
                $L[$i][$j] = max($L[$i-1][$j], $L[$i][$j-1]);
            }
        }
    }
    
    return $L[$m][$n];
}

echo lcs("ABCDGH", "AEDFHR");
?>""")

def complete_remaining_files():
    """Completa arquivos restantes"""
    
    # Matrix Multiplication - pequenos
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/matrix-multiplication"
    
    # Kotlin
    with open(f"{base_dir}/UmatrixUmultiplication.kt", "w") as f:
        f.write("""fun matrixMultiply(a: Array<IntArray>, b: Array<IntArray>): Array<IntArray> {
    val rowsA = a.size
    val colsA = a[0].size
    val colsB = b[0].size
    
    val result = Array(rowsA) { IntArray(colsB) }
    
    for (i in 0 until rowsA) {
        for (j in 0 until colsB) {
            for (k in 0 until colsA) {
                result[i][j] += a[i][k] * b[k][j]
            }
        }
    }
    
    return result
}

fun main() {
    val a = arrayOf(intArrayOf(1, 2), intArrayOf(3, 4))
    val b = arrayOf(intArrayOf(5, 6), intArrayOf(7, 8))
    
    val result = matrixMultiply(a, b)
    result.forEach { row ->
        println(row.joinToString(" "))
    }
}""")

    # PHP
    with open(f"{base_dir}/matrix_multiplication.php", "w") as f:
        f.write("""<?php
function matrixMultiply($a, $b) {
    $rowsA = count($a);
    $colsA = count($a[0]);
    $colsB = count($b[0]);
    
    $result = array_fill(0, $rowsA, array_fill(0, $colsB, 0));
    
    for ($i = 0; $i < $rowsA; $i++) {
        for ($j = 0; $j < $colsB; $j++) {
            for ($k = 0; $k < $colsA; $k++) {
                $result[$i][$j] += $a[$i][$k] * $b[$k][$j];
            }
        }
    }
    
    return $result;
}

$a = [[1, 2], [3, 4]];
$b = [[5, 6], [7, 8]];

$result = matrixMultiply($a, $b);
foreach ($result as $row) {
    echo implode(" ", $row) . "\\n";
}
?>""")

    # Sieve of Eratosthenes - pequenos
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/sieve-of-eratosthenes"
    
    # Kotlin
    with open(f"{base_dir}/UsieveUofUeratosthenes.kt", "w") as f:
        f.write("""fun sieveOfEratosthenes(n: Int): List<Int> {
    val prime = BooleanArray(n + 1) { true }
    prime[0] = false
    if (n > 0) prime[1] = false
    
    var p = 2
    while (p * p <= n) {
        if (prime[p]) {
            var i = p * p
            while (i <= n) {
                prime[i] = false
                i += p
            }
        }
        p++
    }
    
    return (2..n).filter { prime[it] }
}

fun main() {
    println(sieveOfEratosthenes(30))
}""")

    # PHP
    with open(f"{base_dir}/sieve_of_eratosthenes.php", "w") as f:
        f.write("""<?php
function sieveOfEratosthenes($n) {
    $prime = array_fill(0, $n + 1, true);
    $prime[0] = $prime[1] = false;
    
    for ($p = 2; $p * $p <= $n; $p++) {
        if ($prime[$p]) {
            for ($i = $p * $p; $i <= $n; $i += $p) {
                $prime[$i] = false;
            }
        }
    }
    
    $primes = [];
    for ($i = 2; $i <= $n; $i++) {
        if ($prime[$i]) {
            $primes[] = $i;
        }
    }
    
    return $primes;
}

print_r(sieveOfEratosthenes(30));
?>""")

if __name__ == "__main__":
    print("Completando implementações finais...")
    complete_remaining_small_files()
    complete_longest_common_subsequence()
    complete_remaining_files()
    print("Todas as implementações finalizadas!")
