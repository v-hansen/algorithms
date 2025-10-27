use std::collections::{HashMap, BinaryHeap};
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
}