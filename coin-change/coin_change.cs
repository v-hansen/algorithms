using System;
using System.Linq;

class CoinChange {
    static int MinCoins(int[] coins, int amount) {
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
    
    static int CountWays(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        
        foreach (int coin in coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
    
    static void Main() {
        int[] coins = {1, 3, 4};
        Console.WriteLine($"Min coins: {MinCoins(coins, 6)}");
        Console.WriteLine($"Ways: {CountWays(coins, 6)}");
    }
}