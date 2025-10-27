using System;
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
}