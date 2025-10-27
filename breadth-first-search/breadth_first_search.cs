using System;
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
}