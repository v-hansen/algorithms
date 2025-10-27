#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) { return a > b ? a : b; }

int knapsack(int weights[], int values[], int n, int capacity) {
    int **dp = malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = malloc((capacity + 1) * sizeof(int));
    }
    
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (weights[i-1] <= w) {
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w]);
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    int result = dp[n][capacity];
    for (int i = 0; i <= n; i++) free(dp[i]);
    free(dp);
    return result;
}

int main() {
    int weights[] = {2, 1, 3};
    int values[] = {4, 2, 3};
    printf("%d\n", knapsack(weights, values, 3, 4));
    return 0;
}