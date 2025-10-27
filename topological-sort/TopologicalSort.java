import java.util.*;

public class TopologicalSort {
    
    public static List<Integer> topologicalSortDFS(Map<Integer, List<Integer>> graph, int numVertices) {
        boolean[] visited = new boolean[numVertices];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < numVertices; i++) {
            if (!visited[i]) {
                dfs(graph, i, visited, stack);
            }
        }
        
        List<Integer> result = new ArrayList<>();
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        
        return result;
    }
    
    private static void dfs(Map<Integer, List<Integer>> graph, int v, boolean[] visited, Stack<Integer> stack) {
        visited[v] = true;
        
        List<Integer> neighbors = graph.getOrDefault(v, new ArrayList<>());
        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                dfs(graph, neighbor, visited, stack);
            }
        }
        
        stack.push(v);
    }
    
    public static List<Integer> topologicalSortKahn(Map<Integer, List<Integer>> graph, int numVertices) {
        int[] inDegree = new int[numVertices];
        
        // Calculate in-degrees
        for (int u = 0; u < numVertices; u++) {
            List<Integer> neighbors = graph.getOrDefault(u, new ArrayList<>());
            for (int v : neighbors) {
                inDegree[v]++;
            }
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numVertices; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        List<Integer> result = new ArrayList<>();
        
        while (!queue.isEmpty()) {
            int u = queue.poll();
            result.add(u);
            
            List<Integer> neighbors = graph.getOrDefault(u, new ArrayList<>());
            for (int v : neighbors) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }
        
        return result.size() == numVertices ? result : null;
    }
    
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(5, Arrays.asList(2, 0));
        graph.put(4, Arrays.asList(0, 1));
        graph.put(2, Arrays.asList(3));
        graph.put(3, Arrays.asList(1));
        
        int numVertices = 6;
        System.out.println("DFS: " + topologicalSortDFS(graph, numVertices));
        System.out.println("Kahn: " + topologicalSortKahn(graph, numVertices));
    }
}
