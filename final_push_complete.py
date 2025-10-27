#!/usr/bin/env python3
import os
import glob

def complete_all_small_files():
    """Completa todos os arquivos pequenos restantes"""
    
    # Fibonacci - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/fibonacci"
    
    for file_path in glob.glob(f"{base_dir}/*"):
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 500:
            filename = os.path.basename(file_path)
            
            if filename.endswith('.c'):
                with open(file_path, "w") as f:
                    f.write("""#include <stdio.h>
int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n-1) + fibRecursive(n-2);
}

int fibIterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    printf("Recursive: %d\\n", fibRecursive(10));
    printf("Iterative: %d\\n", fibIterative(10));
    return 0;
}""")
            
            elif filename.endswith('.cpp'):
                with open(file_path, "w") as f:
                    f.write("""#include <iostream>
#include <vector>
using namespace std;

int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n-1) + fibRecursive(n-2);
}

int fibIterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int fibMemoized(int n, vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibMemoized(n-1, memo) + fibMemoized(n-2, memo);
    return memo[n];
}

int main() {
    cout << "Recursive: " << fibRecursive(10) << endl;
    cout << "Iterative: " << fibIterative(10) << endl;
    
    vector<int> memo(11, -1);
    cout << "Memoized: " << fibMemoized(10, memo) << endl;
    return 0;
}""")
            
            elif filename.endswith('.go'):
                with open(file_path, "w") as f:
                    f.write("""package main
import "fmt"

func fibRecursive(n int) int {
    if n <= 1 {
        return n
    }
    return fibRecursive(n-1) + fibRecursive(n-2)
}

func fibIterative(n int) int {
    if n <= 1 {
        return n
    }
    a, b := 0, 1
    for i := 2; i <= n; i++ {
        a, b = b, a+b
    }
    return b
}

func fibMemoized(n int, memo map[int]int) int {
    if n <= 1 {
        return n
    }
    if val, exists := memo[n]; exists {
        return val
    }
    memo[n] = fibMemoized(n-1, memo) + fibMemoized(n-2, memo)
    return memo[n]
}

func main() {
    fmt.Printf("Recursive: %d\\n", fibRecursive(10))
    fmt.Printf("Iterative: %d\\n", fibIterative(10))
    
    memo := make(map[int]int)
    fmt.Printf("Memoized: %d\\n", fibMemoized(10, memo))
}""")

    # Euclidean Algorithm - expandir implementações pequenas
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/euclidean-algorithm"
    
    for file_path in glob.glob(f"{base_dir}/*"):
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 200:
            filename = os.path.basename(file_path)
            
            if filename.endswith('.c'):
                with open(file_path, "w") as f:
                    f.write("""#include <stdio.h>
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int gcdRecursive(int a, int b) {
    if (b == 0) return a;
    return gcdRecursive(b, a % b);
}

int main() {
    printf("GCD iterative: %d\\n", gcd(48, 18));
    printf("GCD recursive: %d\\n", gcdRecursive(48, 18));
    return 0;
}""")
            
            elif filename.endswith('.cpp'):
                with open(file_path, "w") as f:
                    f.write("""#include <iostream>
#include <algorithm>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int gcdRecursive(int a, int b) {
    return b == 0 ? a : gcdRecursive(b, a % b);
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    cout << "GCD iterative: " << gcd(48, 18) << endl;
    cout << "GCD recursive: " << gcdRecursive(48, 18) << endl;
    cout << "LCM: " << lcm(48, 18) << endl;
    cout << "STL GCD: " << __gcd(48, 18) << endl;
    return 0;
}""")

def complete_topological_sort():
    """Completa topological sort em todas as linguagens"""
    
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/topological-sort"
    
    topo_implementations = {
        "topological_sort.c": """#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int visited[MAX];
int stack[MAX], top = -1;
int adj[MAX][MAX];

void push(int x) { stack[++top] = x; }
int pop() { return stack[top--]; }

void dfs(int v, int n) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i, n);
        }
    }
    push(v);
}

void topologicalSort(int n) {
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, n);
        }
    }
    
    while (top >= 0) {
        printf("%d ", pop());
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][3] = 1;
    adj[2][3] = 1;
    
    topologicalSort(n);
    return 0;
}""",
        
        "topological_sort.cpp": """#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
using namespace std;

void dfs(int node, const vector<vector<int>>& graph, unordered_set<int>& visited, stack<int>& topoStack) {
    visited.insert(node);
    
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited, topoStack);
        }
    }
    
    topoStack.push(node);
}

vector<int> topologicalSort(const vector<vector<int>>& graph) {
    unordered_set<int> visited;
    stack<int> topoStack;
    
    for (int i = 0; i < graph.size(); i++) {
        if (visited.find(i) == visited.end()) {
            dfs(i, graph, visited, topoStack);
        }
    }
    
    vector<int> result;
    while (!topoStack.empty()) {
        result.push_back(topoStack.top());
        topoStack.pop();
    }
    
    return result;
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {3}, {3}, {}};
    auto result = topologicalSort(graph);
    
    for (int node : result) {
        cout << node << " ";
    }
    cout << endl;
    
    return 0;
}""",
        
        "topological_sort.go": """package main
import "fmt"

func dfs(node int, graph map[int][]int, visited map[int]bool, stack *[]int) {
    visited[node] = true
    
    for _, neighbor := range graph[node] {
        if !visited[neighbor] {
            dfs(neighbor, graph, visited, stack)
        }
    }
    
    *stack = append(*stack, node)
}

func topologicalSort(graph map[int][]int) []int {
    visited := make(map[int]bool)
    var stack []int
    
    for node := range graph {
        if !visited[node] {
            dfs(node, graph, visited, &stack)
        }
    }
    
    // Reverse the stack
    for i, j := 0, len(stack)-1; i < j; i, j = i+1, j-1 {
        stack[i], stack[j] = stack[j], stack[i]
    }
    
    return stack
}

func main() {
    graph := map[int][]int{
        0: {1, 2},
        1: {3},
        2: {3},
        3: {},
    }
    
    result := topologicalSort(graph)
    fmt.Println(result)
}""",
        
        "topological_sort.php": """<?php
function dfs($node, $graph, &$visited, &$stack) {
    $visited[$node] = true;
    
    if (isset($graph[$node])) {
        foreach ($graph[$node] as $neighbor) {
            if (!isset($visited[$neighbor])) {
                dfs($neighbor, $graph, $visited, $stack);
            }
        }
    }
    
    array_push($stack, $node);
}

function topologicalSort($graph) {
    $visited = [];
    $stack = [];
    
    foreach (array_keys($graph) as $node) {
        if (!isset($visited[$node])) {
            dfs($node, $graph, $visited, $stack);
        }
    }
    
    return array_reverse($stack);
}

$graph = [
    0 => [1, 2],
    1 => [3],
    2 => [3],
    3 => []
];

$result = topologicalSort($graph);
print_r($result);
?>""",
        
        "topological_sort.cs": """using System;
using System.Collections.Generic;

class TopologicalSort {
    static void Dfs(int node, Dictionary<int, List<int>> graph, HashSet<int> visited, Stack<int> stack) {
        visited.Add(node);
        
        if (graph.ContainsKey(node)) {
            foreach (int neighbor in graph[node]) {
                if (!visited.Contains(neighbor)) {
                    Dfs(neighbor, graph, visited, stack);
                }
            }
        }
        
        stack.Push(node);
    }
    
    static List<int> Sort(Dictionary<int, List<int>> graph) {
        var visited = new HashSet<int>();
        var stack = new Stack<int>();
        
        foreach (int node in graph.Keys) {
            if (!visited.Contains(node)) {
                Dfs(node, graph, visited, stack);
            }
        }
        
        var result = new List<int>();
        while (stack.Count > 0) {
            result.Add(stack.Pop());
        }
        
        return result;
    }
    
    static void Main() {
        var graph = new Dictionary<int, List<int>> {
            {0, new List<int> {1, 2}},
            {1, new List<int> {3}},
            {2, new List<int> {3}},
            {3, new List<int>()}
        };
        
        var result = Sort(graph);
        Console.WriteLine(string.Join(" ", result));
    }
}"""
    }
    
    for filename, code in topo_implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Fazendo push final para completar tudo...")
    complete_all_small_files()
    complete_topological_sort()
    print("PUSH FINAL COMPLETADO - TUDO FINALIZADO!")
