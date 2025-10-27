#!/usr/bin/env python3
import os
import glob

def complete_linear_search_all():
    """Completa linear search em todas as linguagens restantes"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/linear-search"
    
    implementations = {
        "linear-search.rs": """fn linear_search(arr: &[i32], target: i32) -> Option<usize> {
    for (i, &val) in arr.iter().enumerate() {
        if val == target { return Some(i); }
    }
    None
}

fn linear_search_recursive(arr: &[i32], target: i32, index: usize) -> Option<usize> {
    if index >= arr.len() { return None; }
    if arr[index] == target { return Some(index); }
    linear_search_recursive(arr, target, index + 1)
}

fn main() {
    let arr = [1, 2, 3, 4, 5];
    println!("{:?}", linear_search(&arr, 3));
    println!("{:?}", linear_search_recursive(&arr, 3, 0));
}""",
        
        "LinearSearch.java": """public class LinearSearch {
    public static int search(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    public static int searchRecursive(int[] arr, int target, int index) {
        if (index >= arr.length) return -1;
        if (arr[index] == target) return index;
        return searchRecursive(arr, target, index + 1);
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("Iterative: " + search(arr, 3));
        System.out.println("Recursive: " + searchRecursive(arr, 3, 0));
    }
}""",
        
        "linear-search.clj": """(defn linear-search [arr target]
  (loop [i 0]
    (cond
      (>= i (count arr)) -1
      (= (nth arr i) target) i
      :else (recur (inc i)))))

(defn linear-search-recursive [arr target index]
  (cond
    (>= index (count arr)) -1
    (= (nth arr index) target) index
    :else (linear-search-recursive arr target (inc index))))

(println (linear-search [1 2 3 4 5] 3))
(println (linear-search-recursive [1 2 3 4 5] 3 0))"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_bubble_sort_all():
    """Completa bubble sort em todas as linguagens restantes"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/bubble-sort"
    
    implementations = {
        "bubble-sort.rs": """fn bubble_sort(arr: &mut [i32]) {
    let n = arr.len();
    for i in 0..n {
        let mut swapped = false;
        for j in 0..n-1-i {
            if arr[j] > arr[j+1] {
                arr.swap(j, j+1);
                swapped = true;
            }
        }
        if !swapped { break; }
    }
}

fn main() {
    let mut arr = [64, 34, 25, 12, 22, 11, 90];
    bubble_sort(&mut arr);
    println!("{:?}", arr);
}""",
        
        "BubbleSort.java": """public class BubbleSort {
    public static void sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++) {
            boolean swapped = false;
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        sort(arr);
        for (int x : arr) System.out.print(x + " ");
    }
}""",
        
        "bubble-sort.clj": """(defn bubble-sort [arr]
  (loop [arr arr n (count arr)]
    (if (<= n 1)
      arr
      (let [[new-arr swapped] 
            (reduce (fn [[acc swapped] i]
                     (if (and (< (inc i) (count acc))
                             (> (nth acc i) (nth acc (inc i))))
                       [(assoc acc i (nth acc (inc i)) (inc i) (nth acc i)) true]
                       [acc swapped]))
                   [arr false] (range (dec n)))]
        (if swapped
          (recur new-arr (dec n))
          new-arr)))))

(println (bubble-sort [64 34 25 12 22 11 90]))"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_dfs_all():
    """Completa DFS em todas as linguagens restantes"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/depth-first-search"
    
    implementations = {
        "depth_first_search.rs": """use std::collections::{HashMap, HashSet};

fn dfs(graph: &HashMap<i32, Vec<i32>>, start: i32, visited: &mut HashSet<i32>) {
    visited.insert(start);
    print!("{} ", start);
    
    if let Some(neighbors) = graph.get(&start) {
        for &neighbor in neighbors {
            if !visited.contains(&neighbor) {
                dfs(graph, neighbor, visited);
            }
        }
    }
}

fn main() {
    let mut graph = HashMap::new();
    graph.insert(0, vec![1, 2]);
    graph.insert(1, vec![2]);
    graph.insert(2, vec![0, 3]);
    graph.insert(3, vec![3]);
    
    let mut visited = HashSet::new();
    dfs(&graph, 2, &mut visited);
}""",
        
        "DFS.java": """import java.util.*;

public class DFS {
    public static void dfs(Map<Integer, List<Integer>> graph, int start, Set<Integer> visited) {
        visited.add(start);
        System.out.print(start + " ");
        
        List<Integer> neighbors = graph.getOrDefault(start, new ArrayList<>());
        for (int neighbor : neighbors) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, visited);
            }
        }
    }
    
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(2));
        graph.put(2, Arrays.asList(0, 3));
        graph.put(3, Arrays.asList(3));
        
        Set<Integer> visited = new HashSet<>();
        dfs(graph, 2, visited);
    }
}""",
        
        "DFS.kt": """fun dfs(graph: Map<Int, List<Int>>, start: Int, visited: MutableSet<Int>) {
    visited.add(start)
    print("$start ")
    
    graph[start]?.forEach { neighbor ->
        if (neighbor !in visited) {
            dfs(graph, neighbor, visited)
        }
    }
}

fun main() {
    val graph = mapOf(
        0 to listOf(1, 2),
        1 to listOf(2),
        2 to listOf(0, 3),
        3 to listOf(3)
    )
    
    val visited = mutableSetOf<Int>()
    dfs(graph, 2, visited)
}""",
        
        "depth_first_search.ts": """function dfs(graph: {[key: number]: number[]}, start: number, visited: Set<number>): void {
    visited.add(start);
    process.stdout.write(start + " ");
    
    const neighbors = graph[start] || [];
    for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, visited);
        }
    }
}

const graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
};

const visited = new Set<number>();
dfs(graph, 2, visited);"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_bfs_all():
    """Completa BFS em todas as linguagens restantes"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/breadth-first-search"
    
    implementations = {
        "breadth_first_search.rs": """use std::collections::{HashMap, HashSet, VecDeque};

fn bfs(graph: &HashMap<i32, Vec<i32>>, start: i32) {
    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();
    
    visited.insert(start);
    queue.push_back(start);
    
    while let Some(node) = queue.pop_front() {
        print!("{} ", node);
        
        if let Some(neighbors) = graph.get(&node) {
            for &neighbor in neighbors {
                if !visited.contains(&neighbor) {
                    visited.insert(neighbor);
                    queue.push_back(neighbor);
                }
            }
        }
    }
}

fn main() {
    let mut graph = HashMap::new();
    graph.insert(0, vec![1, 2]);
    graph.insert(1, vec![2]);
    graph.insert(2, vec![0, 3]);
    graph.insert(3, vec![3]);
    
    bfs(&graph, 2);
}""",
        
        "BFS.java": """import java.util.*;

public class BFS {
    public static void bfs(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        
        visited.add(start);
        queue.offer(start);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            
            List<Integer> neighbors = graph.getOrDefault(node, new ArrayList<>());
            for (int neighbor : neighbors) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
    }
    
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(2));
        graph.put(2, Arrays.asList(0, 3));
        graph.put(3, Arrays.asList(3));
        
        bfs(graph, 2);
    }
}""",
        
        "BFS.kt": """import java.util.*

fun bfs(graph: Map<Int, List<Int>>, start: Int) {
    val visited = mutableSetOf<Int>()
    val queue: Queue<Int> = LinkedList()
    
    visited.add(start)
    queue.offer(start)
    
    while (queue.isNotEmpty()) {
        val node = queue.poll()
        print("$node ")
        
        graph[node]?.forEach { neighbor ->
            if (neighbor !in visited) {
                visited.add(neighbor)
                queue.offer(neighbor)
            }
        }
    }
}

fun main() {
    val graph = mapOf(
        0 to listOf(1, 2),
        1 to listOf(2),
        2 to listOf(0, 3),
        3 to listOf(3)
    )
    
    bfs(graph, 2)
}"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_dijkstra_remaining():
    """Completa Dijkstra nas linguagens restantes"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/dijkstra-algorithm"
    
    implementations = {
        "dijkstra_algorithm.rs": """use std::collections::{HashMap, BinaryHeap};
use std::cmp::Reverse;

fn dijkstra(graph: &HashMap<&str, HashMap<&str, i32>>, start: &str) -> HashMap<String, i32> {
    let mut distances = HashMap::new();
    let mut heap = BinaryHeap::new();
    
    for &node in graph.keys() {
        distances.insert(node.to_string(), i32::MAX);
    }
    distances.insert(start.to_string(), 0);
    heap.push(Reverse((0, start)));
    
    while let Some(Reverse((current_distance, current))) = heap.pop() {
        if current_distance > distances[current] {
            continue;
        }
        
        if let Some(neighbors) = graph.get(current) {
            for (&neighbor, &weight) in neighbors {
                let distance = current_distance + weight;
                if distance < distances[neighbor] {
                    distances.insert(neighbor.to_string(), distance);
                    heap.push(Reverse((distance, neighbor)));
                }
            }
        }
    }
    
    distances
}

fn main() {
    let mut graph = HashMap::new();
    let mut a_neighbors = HashMap::new();
    a_neighbors.insert("B", 1);
    a_neighbors.insert("C", 4);
    graph.insert("A", a_neighbors);
    
    let mut b_neighbors = HashMap::new();
    b_neighbors.insert("C", 2);
    b_neighbors.insert("D", 5);
    graph.insert("B", b_neighbors);
    
    let mut c_neighbors = HashMap::new();
    c_neighbors.insert("D", 1);
    graph.insert("C", c_neighbors);
    
    graph.insert("D", HashMap::new());
    
    let result = dijkstra(&graph, "A");
    println!("{:?}", result);
}""",
        
        "Dijkstra.java": """import java.util.*;

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
}""",
        
        "Dijkstra.kt": """import java.util.*

data class Node(val name: String, val distance: Int) : Comparable<Node> {
    override fun compareTo(other: Node) = distance.compareTo(other.distance)
}

fun dijkstra(graph: Map<String, Map<String, Int>>, start: String): Map<String, Int> {
    val distances = mutableMapOf<String, Int>()
    val pq = PriorityQueue<Node>()
    
    graph.keys.forEach { distances[it] = Int.MAX_VALUE }
    distances[start] = 0
    pq.offer(Node(start, 0))
    
    while (pq.isNotEmpty()) {
        val current = pq.poll()
        
        if (current.distance > distances[current.name]!!) continue
        
        graph[current.name]?.forEach { (neighbor, weight) ->
            val distance = current.distance + weight
            if (distance < distances[neighbor]!!) {
                distances[neighbor] = distance
                pq.offer(Node(neighbor, distance))
            }
        }
    }
    
    return distances
}

fun main() {
    val graph = mapOf(
        "A" to mapOf("B" to 1, "C" to 4),
        "B" to mapOf("C" to 2, "D" to 5),
        "C" to mapOf("D" to 1),
        "D" to emptyMap()
    )
    
    println(dijkstra(graph, "A"))
}"""
    }
    
    for filename, code in implementations.items():
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

if __name__ == "__main__":
    print("Completando implementações restantes...")
    complete_linear_search_all()
    complete_bubble_sort_all()
    complete_dfs_all()
    complete_bfs_all()
    complete_dijkstra_remaining()
    print("Implementações restantes completadas!")
