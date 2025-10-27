#!/usr/bin/env python3
import os
import glob

def complete_all_sorting():
    """Completa todos os algoritmos de ordenação"""
    
    # Bubble Sort - todas as linguagens
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/bubble-sort"
    
    bubble_implementations = {
        "bubble-sort.c": """#include <stdio.h>
void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubble_sort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}""",
        
        "bubble-sort.cpp": """#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    bubbleSort(arr);
    for (int x : arr) cout << x << " ";
    return 0;
}""",
        
        "bubble-sort.go": """package main
import "fmt"

func bubbleSort(arr []int) {
    n := len(arr)
    for i := 0; i < n-1; i++ {
        for j := 0; j < n-i-1; j++ {
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
}

func main() {
    arr := []int{64, 34, 25, 12, 22, 11, 90}
    bubbleSort(arr)
    fmt.Println(arr)
}""",
        
        "bubble-sort.php": """<?php
function bubbleSort(&$arr) {
    $n = count($arr);
    for ($i = 0; $i < $n-1; $i++) {
        for ($j = 0; $j < $n-$i-1; $j++) {
            if ($arr[$j] > $arr[$j+1]) {
                $temp = $arr[$j];
                $arr[$j] = $arr[$j+1];
                $arr[$j+1] = $temp;
            }
        }
    }
}

$arr = [64, 34, 25, 12, 22, 11, 90];
bubbleSort($arr);
print_r($arr);
?>"""
    }
    
    for filename, code in bubble_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

    # Quick Sort - completar placeholders
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/quick-sort"
    
    # PHP
    with open(f"{base_dir}/quick_sort.php", "w") as f:
        f.write("""<?php
function quickSort($arr) {
    if (count($arr) <= 1) return $arr;
    
    $pivot = $arr[0];
    $less = $greater = [];
    
    for ($i = 1; $i < count($arr); $i++) {
        if ($arr[$i] < $pivot) {
            $less[] = $arr[$i];
        } else {
            $greater[] = $arr[$i];
        }
    }
    
    return array_merge(quickSort($less), [$pivot], quickSort($greater));
}

$arr = [64, 34, 25, 12, 22, 11, 90];
print_r(quickSort($arr));
?>""")

    # C#
    with open(f"{base_dir}/quick_sort.cs", "w") as f:
        f.write("""using System;
using System.Linq;

class QuickSort {
    static int[] Sort(int[] arr) {
        if (arr.Length <= 1) return arr;
        
        int pivot = arr[0];
        var less = arr.Skip(1).Where(x => x < pivot).ToArray();
        var greater = arr.Skip(1).Where(x => x >= pivot).ToArray();
        
        return Sort(less).Concat(new[] { pivot }).Concat(Sort(greater)).ToArray();
    }
    
    static void Main() {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        var sorted = Sort(arr);
        Console.WriteLine(string.Join(" ", sorted));
    }
}""")

def complete_all_search():
    """Completa todos os algoritmos de busca"""
    
    # Linear Search - expandir todas as implementações
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-search"
    
    linear_implementations = {
        "linear-search.c": """#include <stdio.h>
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("%d\\n", linearSearch(arr, n, 3));
    return 0;
}""",
        
        "linear-search.cpp": """#include <iostream>
#include <vector>
using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << linearSearch(arr, 3) << endl;
    return 0;
}""",
        
        "linear-search.go": """package main
import "fmt"

func linearSearch(arr []int, target int) int {
    for i, val := range arr {
        if val == target {
            return i
        }
    }
    return -1
}

func main() {
    arr := []int{1, 2, 3, 4, 5}
    fmt.Println(linearSearch(arr, 3))
}""",
        
        "linear-search.php": """<?php
function linearSearch($arr, $target) {
    for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] == $target) return $i;
    }
    return -1;
}

$arr = [1, 2, 3, 4, 5];
echo linearSearch($arr, 3);
?>""",
        
        "linear-search.cs": """using System;

class LinearSearch {
    static int Search(int[] arr, int target) {
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    static void Main() {
        int[] arr = {1, 2, 3, 4, 5};
        Console.WriteLine(Search(arr, 3));
    }
}"""
    }
    
    for filename, code in linear_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_all_graph_algorithms():
    """Completa todos os algoritmos de grafos"""
    
    # DFS - completar placeholders
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/depth-first-search"
    
    dfs_implementations = {
        "depth_first_search.c": """#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int visited[MAX];
int adj[MAX][MAX];

void dfs(int v, int n) {
    visited[v] = 1;
    printf("%d ", v);
    
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i, n);
        }
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][2] = 1;
    adj[2][0] = adj[2][3] = 1;
    adj[3][3] = 1;
    
    dfs(2, n);
    return 0;
}""",
        
        "depth_first_search.cpp": """#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(int node, const vector<vector<int>>& graph, unordered_set<int>& visited) {
    visited.insert(node);
    cout << node << " ";
    
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited);
        }
    }
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {2}, {0, 3}, {3}};
    unordered_set<int> visited;
    dfs(2, graph, visited);
    return 0;
}""",
        
        "depth_first_search.go": """package main
import "fmt"

func dfs(graph map[int][]int, start int, visited map[int]bool) {
    visited[start] = true
    fmt.Print(start, " ")
    
    for _, neighbor := range graph[start] {
        if !visited[neighbor] {
            dfs(graph, neighbor, visited)
        }
    }
}

func main() {
    graph := map[int][]int{
        0: {1, 2},
        1: {2},
        2: {0, 3},
        3: {3},
    }
    visited := make(map[int]bool)
    dfs(graph, 2, visited)
}""",
        
        "depth_first_search.php": """<?php
function dfs($graph, $start, &$visited) {
    $visited[$start] = true;
    echo $start . " ";
    
    if (isset($graph[$start])) {
        foreach ($graph[$start] as $neighbor) {
            if (!isset($visited[$neighbor])) {
                dfs($graph, $neighbor, $visited);
            }
        }
    }
}

$graph = [
    0 => [1, 2],
    1 => [2],
    2 => [0, 3],
    3 => [3]
];
$visited = [];
dfs($graph, 2, $visited);
?>""",
        
        "depth_first_search.cs": """using System;
using System.Collections.Generic;

class DFS {
    static void Dfs(Dictionary<int, List<int>> graph, int start, HashSet<int> visited) {
        visited.Add(start);
        Console.Write(start + " ");
        
        if (graph.ContainsKey(start)) {
            foreach (int neighbor in graph[start]) {
                if (!visited.Contains(neighbor)) {
                    Dfs(graph, neighbor, visited);
                }
            }
        }
    }
    
    static void Main() {
        var graph = new Dictionary<int, List<int>> {
            {0, new List<int> {1, 2}},
            {1, new List<int> {2}},
            {2, new List<int> {0, 3}},
            {3, new List<int> {3}}
        };
        var visited = new HashSet<int>();
        Dfs(graph, 2, visited);
    }
}"""
    }
    
    for filename, code in dfs_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando TODAS as implementações restantes...")
    complete_all_sorting()
    complete_all_search()
    complete_all_graph_algorithms()
    print("Primeira fase de completamento finalizada!")
