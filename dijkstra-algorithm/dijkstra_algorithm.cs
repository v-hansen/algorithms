using System;
using System.Collections.Generic;

class Dijkstra {
    static Dictionary<string, int> DijkstraAlgorithm(Dictionary<string, Dictionary<string, int>> graph, string start) {
        var distances = new Dictionary<string, int>();
        var pq = new List<(string node, int distance)>();
        
        foreach (var node in graph.Keys) {
            distances[node] = int.MaxValue;
        }
        distances[start] = 0;
        pq.Add((start, 0));
        
        while (pq.Count > 0) {
            pq.Sort((a, b) => a.distance.CompareTo(b.distance));
            var (current, currentDistance) = pq[0];
            pq.RemoveAt(0);
            
            if (currentDistance > distances[current]) continue;
            
            foreach (var neighbor in graph[current]) {
                int distance = currentDistance + neighbor.Value;
                if (distance < distances[neighbor.Key]) {
                    distances[neighbor.Key] = distance;
                    pq.Add((neighbor.Key, distance));
                }
            }
        }
        
        return distances;
    }
    
    static void Main() {
        var graph = new Dictionary<string, Dictionary<string, int>> {
            {"A", new Dictionary<string, int> {{"B", 1}, {"C", 4}}},
            {"B", new Dictionary<string, int> {{"C", 2}, {"D", 5}}},
            {"C", new Dictionary<string, int> {{"D", 1}}},
            {"D", new Dictionary<string, int>()}
        };
        
        var result = DijkstraAlgorithm(graph, "A");
        foreach (var kvp in result) {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
    }
}