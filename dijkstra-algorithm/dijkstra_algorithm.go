package main
import (
    "fmt"
    "math"
)

func dijkstra(graph [][]int, src int) []int {
    V := len(graph)
    dist := make([]int, V)
    sptSet := make([]bool, V)
    
    for i := 0; i < V; i++ {
        dist[i] = math.MaxInt32
    }
    dist[src] = 0
    
    for count := 0; count < V-1; count++ {
        u := minDistance(dist, sptSet)
        sptSet[u] = true
        
        for v := 0; v < V; v++ {
            if !sptSet[v] && graph[u][v] != 0 && dist[u] != math.MaxInt32 && dist[u]+graph[u][v] < dist[v] {
                dist[v] = dist[u] + graph[u][v]
            }
        }
    }
    
    return dist
}

func minDistance(dist []int, sptSet []bool) int {
    min := math.MaxInt32
    minIndex := 0
    
    for v := 0; v < len(dist); v++ {
        if !sptSet[v] && dist[v] <= min {
            min = dist[v]
            minIndex = v
        }
    }
    
    return minIndex
}

func main() {
    graph := [][]int{
        {0, 1, 4, 0},
        {1, 0, 2, 5},
        {4, 2, 0, 1},
        {0, 5, 1, 0},
    }
    
    result := dijkstra(graph, 0)
    for i, d := range result {
        fmt.Printf("%d: %d\n", i, d)
    }
}