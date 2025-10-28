import java.util.*;

public class DFSTest {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(3));
        graph.put(2, Arrays.asList(4));
        graph.put(3, new ArrayList<>());
        graph.put(4, new ArrayList<>());
        
        Set<Integer> visited = DepthFirstSearch.dfs(graph, 0);
        assert visited.size() == 5 : "DFS failed";
        System.out.println("DFSTest passed");
    }
}
