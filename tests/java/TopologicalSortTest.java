import java.util.*;

public class TopologicalSortTest {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(5, Arrays.asList(2, 0));
        graph.put(4, Arrays.asList(0, 1));
        graph.put(2, Arrays.asList(3));
        graph.put(3, Arrays.asList(1));
        graph.put(0, new ArrayList<>());
        graph.put(1, new ArrayList<>());
        
        List<Integer> result = TopologicalSort.topologicalSortDFS(graph, 6);
        assert result.size() == 6 : "Topological sort failed";
        System.out.println("TopologicalSortTest passed");
    }
}
