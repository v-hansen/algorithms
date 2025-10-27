#include <stdio.h>
#include <limits.h>

int min(int a, int b) { return a < b ? a : b; }

int coinChange(int coins[], int m, int amount) {
    int dp[amount + 1];
    dp[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        dp[i] = INT_MAX;
        for (int j = 0; j < m; j++) {
            if (coins[j] <= i && dp[i - coins[j]] != INT_MAX) {
                dp[i] = min(dp[i], dp[i - coins[j]] + 1);
            }
        }
    }
    
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    int coins[] = {1, 3, 4};
    printf("%d\n", coinChange(coins, 3, 6));
    return 0;
}