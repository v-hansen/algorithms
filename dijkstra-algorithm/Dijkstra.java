import java.util.*;

public class Dijkstra {
    public static Map<String, Integer> dijkstra(Map<String, Map<String, Integer>> graph, String start) {
        Map<String, Integer> distances = new HashMap<>();
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        for (String node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            
            if (current.distance > distances.get(current.name)) {
                continue;
            }
            
            Map<String, Integer> neighbors = graph.getOrDefault(current.name, new HashMap<>());
            for (Map.Entry<String, Integer> neighbor : neighbors.entrySet()) {
                int distance = current.distance + neighbor.getValue();
                if (distance < distances.get(neighbor.getKey())) {
                    distances.put(neighbor.getKey(), distance);
                    pq.offer(new Node(neighbor.getKey(), distance));
                }
            }
        }
        
        return distances;
    }
    
    static class Node implements Comparable<Node> {
        String name;
        int distance;
        
        Node(String name, int distance) {
            this.name = name;
            this.distance = distance;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.distance, other.distance);
        }
    }
    
    public static void main(String[] args) {
        Map<String, Map<String, Integer>> graph = new HashMap<>();
        
        Map<String, Integer> aNeighbors = new HashMap<>();
        aNeighbors.put("B", 1);
        aNeighbors.put("C", 4);
        graph.put("A", aNeighbors);
        
        Map<String, Integer> bNeighbors = new HashMap<>();
        bNeighbors.put("C", 2);
        bNeighbors.put("D", 5);
        graph.put("B", bNeighbors);
        
        Map<String, Integer> cNeighbors = new HashMap<>();
        cNeighbors.put("D", 1);
        graph.put("C", cNeighbors);
        
        graph.put("D", new HashMap<>());
        
        Map<String, Integer> result = dijkstra(graph, "A");
        System.out.println(result);
    }
}