package main
import "fmt"

func max(a, b int) int {
    if a > b { return a }
    return b
}

func knapsack(weights, values []int, capacity int) int {
    n := len(weights)
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, capacity+1)
    }
    
    for i := 1; i <= n; i++ {
        for w := 1; w <= capacity; w++ {
            if weights[i-1] <= w {
                dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]], dp[i-1][w])
            } else {
                dp[i][w] = dp[i-1][w]
            }
        }
    }
    
    return dp[n][capacity]
}

func knapsackOptimized(weights, values []int, capacity int) int {
    dp := make([]int, capacity+1)
    
    for i := 0; i < len(weights); i++ {
        for w := capacity; w >= weights[i]; w-- {
            dp[w] = max(dp[w], dp[w-weights[i]]+values[i])
        }
    }
    
    return dp[capacity]
}

func main() {
    weights := []int{2, 1, 3}
    values := []int{4, 2, 3}
    fmt.Printf("2D DP: %d\n", knapsack(weights, values, 4))
    fmt.Printf("1D DP: %d\n", knapsackOptimized(weights, values, 4))
}