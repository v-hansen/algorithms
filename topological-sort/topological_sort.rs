use std::collections::{HashMap, HashSet};

fn topological_sort(graph: &HashMap<i32, Vec<i32>>) -> Vec<i32> {
    let mut visited = HashSet::new();
    let mut stack = Vec::new();
    
    fn dfs(node: i32, graph: &HashMap<i32, Vec<i32>>, visited: &mut HashSet<i32>, stack: &mut Vec<i32>) {
        if visited.contains(&node) {
            return;
        }
        
        visited.insert(node);
        
        if let Some(neighbors) = graph.get(&node) {
            for &neighbor in neighbors {
                dfs(neighbor, graph, visited, stack);
            }
        }
        
        stack.push(node);
    }
    
    for &node in graph.keys() {
        dfs(node, graph, &mut visited, &mut stack);
    }
    
    stack.reverse();
    stack
}

fn main() {
    let mut graph = HashMap::new();
    graph.insert(0, vec![1, 2]);
    graph.insert(1, vec![3]);
    graph.insert(2, vec![3]);
    graph.insert(3, vec![]);
    
    println!("{:?}", topological_sort(&graph));
}