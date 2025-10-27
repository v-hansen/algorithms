import java.util.*;

public class CoinChange {
    
    public static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                if (dp[i - coin] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }
    
    public static int coinChangeWays(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        
        return dp[amount];
    }
    
    public static class CoinChangeResult {
        public int minCoins;
        public List<Integer> coins;
        
        public CoinChangeResult(int minCoins, List<Integer> coins) {
            this.minCoins = minCoins;
            this.coins = coins;
        }
    }
    
    public static CoinChangeResult coinChangeWithCoins(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        int[] parent = new int[amount + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i && dp[i - coin] != Integer.MAX_VALUE && dp[i - coin] + 1 < dp[i]) {
                    dp[i] = dp[i - coin] + 1;
                    parent[i] = coin;
                }
            }
        }
        
        if (dp[amount] == Integer.MAX_VALUE) {
            return new CoinChangeResult(-1, new ArrayList<>());
        }
        
        // Reconstruct solution
        List<Integer> resultCoins = new ArrayList<>();
        int curr = amount;
        while (curr > 0) {
            int coin = parent[curr];
            resultCoins.add(coin);
            curr -= coin;
        }
        
        return new CoinChangeResult(dp[amount], resultCoins);
    }
    
    public static void main(String[] args) {
        int[] coins = {1, 3, 4};
        int amount = 6;
        System.out.println("Min coins for " + amount + ": " + coinChange(coins, amount)); // 2
        System.out.println("Ways to make " + amount + ": " + coinChangeWays(coins, amount)); // 2
    }
}
