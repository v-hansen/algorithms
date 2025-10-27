using System;
using System.Linq;

class DynamicProgramming {
    static int Fibonacci(int n) {
        if (n <= 1) return n;
        int[] dp = new int[n + 1];
        dp[0] = 0; dp[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
    
    static int CoinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Array.Fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            foreach (int coin in coins) {
                if (coin <= i) {
                    dp[i] = Math.Min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] > amount ? -1 : dp[amount];
    }
    
    static int Knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.Length;
        int[,] dp = new int[n + 1, capacity + 1];
        
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i-1] <= w) {
                    dp[i,w] = Math.Max(dp[i-1,w], dp[i-1,w-weights[i-1]] + values[i-1]);
                } else {
                    dp[i,w] = dp[i-1,w];
                }
            }
        }
        return dp[n,capacity];
    }
    
    static void Main() {
        Console.WriteLine($"Fibonacci(10): {Fibonacci(10)}");
        Console.WriteLine($"Coin change: {CoinChange(new int[]{1, 3, 4}, 6)}");
        Console.WriteLine($"Knapsack: {Knapsack(new int[]{2, 1, 3}, new int[]{4, 2, 3}, 4)}");
    }
}