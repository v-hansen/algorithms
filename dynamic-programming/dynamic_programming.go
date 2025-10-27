package main
import "fmt"

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    dp := make([]int, n+1)
    dp[0], dp[1] = 0, 1
    for i := 2; i <= n; i++ {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    for i := 1; i <= amount; i++ {
        dp[i] = amount + 1
    }
    
    for i := 1; i <= amount; i++ {
        for _, coin := range coins {
            if coin <= i {
                if dp[i-coin]+1 < dp[i] {
                    dp[i] = dp[i-coin] + 1
                }
            }
        }
    }
    
    if dp[amount] > amount {
        return -1
    }
    return dp[amount]
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
                include := dp[i-1][w-weights[i-1]] + values[i-1]
                exclude := dp[i-1][w]
                if include > exclude {
                    dp[i][w] = include
                } else {
                    dp[i][w] = exclude
                }
            } else {
                dp[i][w] = dp[i-1][w]
            }
        }
    }
    return dp[n][capacity]
}

func main() {
    fmt.Printf("Fibonacci(10): %d\n", fibonacci(10))
    fmt.Printf("Coin change: %d\n", coinChange([]int{1, 3, 4}, 6))
    fmt.Printf("Knapsack: %d\n", knapsack([]int{2, 1, 3}, []int{4, 2, 3}, 4))
}