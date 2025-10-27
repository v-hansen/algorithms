package main
import "fmt"

func bfs(graph map[int][]int, start int) {
    visited := make(map[int]bool)
    queue := []int{start}
    visited[start] = true
    
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        fmt.Print(node, " ")
        
        for _, neighbor := range graph[node] {
            if !visited[neighbor] {
                visited[neighbor] = true
                queue = append(queue, neighbor)
            }
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
    bfs(graph, 2)
}