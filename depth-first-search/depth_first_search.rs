use std::collections::{HashMap, HashSet};

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
}