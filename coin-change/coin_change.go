package main
import "fmt"

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

func coinChangeWays(coins []int, amount int) int {
    dp := make([]int, amount+1)
    dp[0] = 1
    
    for _, coin := range coins {
        for i := coin; i <= amount; i++ {
            dp[i] += dp[i-coin]
        }
    }
    
    return dp[amount]
}

func main() {
    coins := []int{1, 3, 4}
    fmt.Printf("Min coins: %d\n", coinChange(coins, 6))
    fmt.Printf("Ways: %d\n", coinChangeWays(coins, 6))
}