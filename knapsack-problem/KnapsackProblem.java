import java.util.*;

public class KnapsackProblem {
    
    public static int knapsack01(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        
        // Create DP table
        int[][] dp = new int[n + 1][capacity + 1];
        
        // Fill DP table
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i-1] > w) {
                    dp[i][w] = dp[i-1][w];
                } else {
                    dp[i][w] = Math.max(
                        dp[i-1][w],
                        values[i-1] + dp[i-1][w - weights[i-1]]
                    );
                }
            }
        }
        
        return dp[n][capacity];
    }
    
    public static class KnapsackResult {
        public int maxValue;
        public List<Integer> items;
        
        public KnapsackResult(int maxValue, List<Integer> items) {
            this.maxValue = maxValue;
            this.items = items;
        }
    }
    
    public static KnapsackResult knapsackWithItems(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        int[][] dp = new int[n + 1][capacity + 1];
        
        // Fill DP table
        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i-1] > w) {
                    dp[i][w] = dp[i-1][w];
                } else {
                    dp[i][w] = Math.max(
                        dp[i-1][w],
                        values[i-1] + dp[i-1][w - weights[i-1]]
                    );
                }
            }
        }
        
        // Backtrack to find selected items
        List<Integer> selectedItems = new ArrayList<>();
        int w = capacity;
        for (int i = n; i > 0; i--) {
            if (dp[i][w] != dp[i-1][w]) {
                selectedItems.add(i-1);
                w -= weights[i-1];
            }
        }
        
        Collections.reverse(selectedItems);
        return new KnapsackResult(dp[n][capacity], selectedItems);
    }
    
    public static int knapsackOptimized(int[] weights, int[] values, int capacity) {
        int n = weights.length;
        int[] dp = new int[capacity + 1];
        
        for (int i = 0; i < n; i++) {
            for (int w = capacity; w >= weights[i]; w--) {
                dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
            }
        }
        
        return dp[capacity];
    }
    
    public static void main(String[] args) {
        int[] weights = {1, 3, 4, 5};
        int[] values = {1, 4, 5, 7};
        int capacity = 7;
        
        int maxValue = knapsack01(weights, values, capacity);
        System.out.println("Maximum value: " + maxValue); // 9
        
        KnapsackResult result = knapsackWithItems(weights, values, capacity);
        System.out.println("Maximum value: " + result.maxValue + ", Items: " + result.items); // 9, [1, 2]
    }
}
