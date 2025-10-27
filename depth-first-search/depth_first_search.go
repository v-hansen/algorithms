package main
import "fmt"

func dfs(graph map[int][]int, start int, visited map[int]bool) {
    visited[start] = true
    fmt.Print(start, " ")
    
    for _, neighbor := range graph[start] {
        if !visited[neighbor] {
            dfs(graph, neighbor, visited)
        }
    }
}

func main() {
    graph := map[int][]int{
        0: {1, 2},
        1: {2},
        2: {0, 3},
        3: {3},
    }
    visited := make(map[int]bool)
    dfs(graph, 2, visited)
}