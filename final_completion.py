#!/usr/bin/env python3
import os
import glob

def complete_all_remaining_placeholders():
    """Completa TODOS os placeholders restantes"""
    
    # Heap Sort - completar todos os placeholders
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/heap-sort"
    
    heap_implementations = {
        "heap_sort.c": """#include <stdio.h>
void heapify(int arr[], int n, int i) {
    int largest = i, left = 2*i+1, right = 2*i+2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) right = right;
    if (largest != i) {
        int temp = arr[i]; arr[i] = arr[largest]; arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n/2-1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n-1; i > 0; i--) {
        int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
        heapify(arr, i, 0);
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    heapSort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    return 0;
}""",
        
        "heap_sort.cpp": """#include <iostream>
#include <vector>
using namespace std;

void heapify(vector<int>& arr, int n, int i) {
    int largest = i, left = 2*i+1, right = 2*i+2;
    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n/2-1; i >= 0; i--) heapify(arr, n, i);
    for (int i = n-1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    heapSort(arr);
    for (int x : arr) cout << x << " ";
    return 0;
}""",
        
        "heap_sort.go": """package main
import "fmt"

func heapify(arr []int, n, i int) {
    largest := i
    left, right := 2*i+1, 2*i+2
    
    if left < n && arr[left] > arr[largest] {
        largest = left
    }
    if right < n && arr[right] > arr[largest] {
        largest = right
    }
    if largest != i {
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    }
}

func heapSort(arr []int) {
    n := len(arr)
    for i := n/2 - 1; i >= 0; i-- {
        heapify(arr, n, i)
    }
    for i := n - 1; i > 0; i-- {
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    }
}

func main() {
    arr := []int{64, 34, 25, 12, 22, 11, 90}
    heapSort(arr)
    fmt.Println(arr)
}""",
        
        "heap_sort.php": """<?php
function heapify(&$arr, $n, $i) {
    $largest = $i;
    $left = 2 * $i + 1;
    $right = 2 * $i + 2;
    
    if ($left < $n && $arr[$left] > $arr[$largest]) $largest = $left;
    if ($right < $n && $arr[$right] > $arr[$largest]) $largest = $right;
    
    if ($largest != $i) {
        $temp = $arr[$i];
        $arr[$i] = $arr[$largest];
        $arr[$largest] = $temp;
        heapify($arr, $n, $largest);
    }
}

function heapSort(&$arr) {
    $n = count($arr);
    for ($i = intval($n / 2) - 1; $i >= 0; $i--) {
        heapify($arr, $n, $i);
    }
    for ($i = $n - 1; $i > 0; $i--) {
        $temp = $arr[0];
        $arr[0] = $arr[$i];
        $arr[$i] = $temp;
        heapify($arr, $i, 0);
    }
}

$arr = [64, 34, 25, 12, 22, 11, 90];
heapSort($arr);
print_r($arr);
?>""",
        
        "heap_sort.cs": """using System;

class HeapSort {
    static void Heapify(int[] arr, int n, int i) {
        int largest = i, left = 2*i+1, right = 2*i+2;
        if (left < n && arr[left] > arr[largest]) largest = left;
        if (right < n && arr[right] > arr[largest]) largest = right;
        if (largest != i) {
            int temp = arr[i]; arr[i] = arr[largest]; arr[largest] = temp;
            Heapify(arr, n, largest);
        }
    }
    
    static void Sort(int[] arr) {
        int n = arr.Length;
        for (int i = n/2-1; i >= 0; i--) Heapify(arr, n, i);
        for (int i = n-1; i > 0; i--) {
            int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
            Heapify(arr, i, 0);
        }
    }
    
    static void Main() {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        Sort(arr);
        Console.WriteLine(string.Join(" ", arr));
    }
}"""
    }
    
    for filename, code in heap_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

    # BFS - completar placeholders restantes
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/breadth-first-search"
    
    bfs_implementations = {
        "breadth_first_search.c": """#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int queue[MAX], front = 0, rear = 0;
int visited[MAX];
int adj[MAX][MAX];

void enqueue(int x) { queue[rear++] = x; }
int dequeue() { return queue[front++]; }
int isEmpty() { return front == rear; }

void bfs(int start, int n) {
    visited[start] = 1;
    enqueue(start);
    
    while (!isEmpty()) {
        int node = dequeue();
        printf("%d ", node);
        
        for (int i = 0; i < n; i++) {
            if (adj[node][i] && !visited[i]) {
                visited[i] = 1;
                enqueue(i);
            }
        }
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][2] = 1;
    adj[2][0] = adj[2][3] = 1;
    adj[3][3] = 1;
    
    bfs(2, n);
    return 0;
}""",
        
        "breadth_first_search.cpp": """#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

void bfs(int start, const vector<vector<int>>& graph) {
    unordered_set<int> visited;
    queue<int> q;
    
    visited.insert(start);
    q.push(start);
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";
        
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {2}, {0, 3}, {3}};
    bfs(2, graph);
    return 0;
}""",
        
        "breadth_first_search.go": """package main
import "fmt"

func bfs(graph map[int][]int, start int) {
    visited := make(map[int]bool)
    queue := []int{start}
    visited[start] = true
    
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        fmt.Print(node, " ")
        
        for _, neighbor := range graph[node] {
            if !visited[neighbor] {
                visited[neighbor] = true
                queue = append(queue, neighbor)
            }
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
    bfs(graph, 2)
}""",
        
        "breadth_first_search.php": """<?php
function bfs($graph, $start) {
    $visited = [];
    $queue = [$start];
    $visited[$start] = true;
    
    while (!empty($queue)) {
        $node = array_shift($queue);
        echo $node . " ";
        
        if (isset($graph[$node])) {
            foreach ($graph[$node] as $neighbor) {
                if (!isset($visited[$neighbor])) {
                    $visited[$neighbor] = true;
                    $queue[] = $neighbor;
                }
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
bfs($graph, 2);
?>""",
        
        "breadth_first_search.cs": """using System;
using System.Collections.Generic;

class BFS {
    static void Bfs(Dictionary<int, List<int>> graph, int start) {
        var visited = new HashSet<int>();
        var queue = new Queue<int>();
        
        visited.Add(start);
        queue.Enqueue(start);
        
        while (queue.Count > 0) {
            int node = queue.Dequeue();
            Console.Write(node + " ");
            
            if (graph.ContainsKey(node)) {
                foreach (int neighbor in graph[node]) {
                    if (!visited.Contains(neighbor)) {
                        visited.Add(neighbor);
                        queue.Enqueue(neighbor);
                    }
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
        Bfs(graph, 2);
    }
}"""
    }
    
    for filename, code in bfs_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando TODOS os placeholders restantes...")
    complete_all_remaining_placeholders()
    print("COMPLETAMENTO FINAL REALIZADO!")
