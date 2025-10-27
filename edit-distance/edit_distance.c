#include <stdio.h>
#include <string.h>

int min(int a, int b, int c) {
    int min_ab = a < b ? a : b;
    return min_ab < c ? min_ab : c;
}

int editDistance(char* str1, char* str2) {
    int m = strlen(str1), n = strlen(str2);
    int dp[m + 1][n + 1];
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
            }
        }
    }
    
    return dp[m][n];
}

int main() {
    printf("%d\n", editDistance("kitten", "sitting"));
    return 0;
}
