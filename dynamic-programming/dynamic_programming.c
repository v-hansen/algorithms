#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n) {
    if (n <= 1) return n;
    int dp[n+1];
    dp[0] = 0; dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}

int coinChange(int coins[], int m, int amount) {
    int dp[amount + 1];
    dp[0] = 0;
    for (int i = 1; i <= amount; i++) dp[i] = amount + 1;
    
    for (int i = 1; i <= amount; i++) {
        for (int j = 0; j < m; j++) {
            if (coins[j] <= i) {
                dp[i] = dp[i] < dp[i - coins[j]] + 1 ? dp[i] : dp[i - coins[j]] + 1;
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

int main() {
    printf("Fibonacci(10): %d\n", fibonacci(10));
    int coins[] = {1, 3, 4};
    printf("Coin change: %d\n", coinChange(coins, 3, 6));
    return 0;
}