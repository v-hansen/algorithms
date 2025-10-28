import java.util.*;

public class BFSTest {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(3));
        graph.put(2, Arrays.asList(4));
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        
        BreadthFirstSearch.bfs(graph, 0);
        System.out.println("BFSTest passed");
    }
}
