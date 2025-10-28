import java.util.*;

public class DijkstraTest {
    public static void main(String[] args) {
        Map<String, Map<String, Integer>> graph = new HashMap<>();
        graph.put("A", new HashMap<String, Integer>() {{ put("B", 1); put("C", 4); }});
        graph.put("B", new HashMap<String, Integer>() {{ put("C", 2); put("D", 5); }});
        graph.put("C", new HashMap<String, Integer>() {{ put("D", 1); }});
        graph.put("D", new HashMap<>());
        
        Map<String, Integer> result = DijkstraAlgorithm.dijkstra(graph, "A");
        assert result.get("D") == 4 : "Dijkstra failed";
        System.out.println("DijkstraTest passed");
    }
}
