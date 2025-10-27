using System;
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
}