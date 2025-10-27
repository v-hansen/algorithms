using System;

class KnapsackProblem {
    static int Knapsack(int[] weights, int[] values, int capacity) {
        int n = weights.Length;
        int[,] dp = new int[n + 1, capacity + 1];
        
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i-1] <= w) {
                    dp[i,w] = Math.Max(values[i-1] + dp[i-1,w-weights[i-1]], dp[i-1,w]);
                } else {
                    dp[i,w] = dp[i-1,w];
                }
            }
        }
        
        return dp[n,capacity];
    }
    
    static int KnapsackOptimized(int[] weights, int[] values, int capacity) {
        int[] dp = new int[capacity + 1];
        
        for (int i = 0; i < weights.Length; i++) {
            for (int w = capacity; w >= weights[i]; w--) {
                dp[w] = Math.Max(dp[w], dp[w - weights[i]] + values[i]);
            }
        }
        
        return dp[capacity];
    }
    
    static void Main() {
        int[] weights = {2, 1, 3};
        int[] values = {4, 2, 3};
        Console.WriteLine($"2D DP: {Knapsack(weights, values, 4)}");
        Console.WriteLine($"1D DP: {KnapsackOptimized(weights, values, 4)}");
    }
}