package main
import "fmt"

func dfs(node int, graph map[int][]int, visited map[int]bool, stack *[]int) {
    visited[node] = true
    
    for _, neighbor := range graph[node] {
        if !visited[neighbor] {
            dfs(neighbor, graph, visited, stack)
        }
    }
    
    *stack = append(*stack, node)
}

func topologicalSort(graph map[int][]int) []int {
    visited := make(map[int]bool)
    var stack []int
    
    for node := range graph {
        if !visited[node] {
            dfs(node, graph, visited, &stack)
        }
    }
    
    // Reverse the stack
    for i, j := 0, len(stack)-1; i < j; i, j = i+1, j-1 {
        stack[i], stack[j] = stack[j], stack[i]
    }
    
    return stack
}

func main() {
    graph := map[int][]int{
        0: {1, 2},
        1: {3},
        2: {3},
        3: {},
    }
    
    result := topologicalSort(graph)
    fmt.Println(result)
}