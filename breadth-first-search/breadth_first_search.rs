use std::collections::{HashMap, HashSet, VecDeque};

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
}