public class EditDistance {
    
    public static int editDistance(String str1, String str2) {
        int m = str1.length();
        int n = str2.length();
        
        // Create DP table
        int[][] dp = new int[m + 1][n + 1];
        
        // Initialize base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = 1 + Math.min(
                        Math.min(dp[i-1][j], dp[i][j-1]),
                        dp[i-1][j-1]
                    );
                }
            }
        }
        
        return dp[m][n];
    }
    
    public static int editDistanceOptimized(String str1, String str2) {
        int m = str1.length();
        int n = str2.length();
        
        // Use only two arrays for space optimization
        int[] prev = new int[n + 1];
        int[] curr = new int[n + 1];
        
        // Initialize first row
        for (int j = 0; j <= n; j++) {
            prev[j] = j;
        }
        
        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            for (int j = 1; j <= n; j++) {
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    curr[j] = prev[j-1];
                } else {
                    curr[j] = 1 + Math.min(
                        Math.min(prev[j], curr[j-1]),
                        prev[j-1]
                    );
                }
            }
            // Swap arrays
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }
        
        return prev[n];
    }
    
    public static void main(String[] args) {
        String str1 = "kitten";
        String str2 = "sitting";
        int distance = editDistance(str1, str2);
        System.out.println("Edit distance between '" + str1 + "' and '" + str2 + "': " + distance); // 3
    }
}
