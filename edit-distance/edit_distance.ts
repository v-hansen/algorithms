function editDistance(str1: string, str2: string): number {
    const m = str1.length;
    const n = str2.length;
    
    const dp: number[][] = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));
    
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i-1] === str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + Math.min(
                    dp[i-1][j],    // deletion
                    dp[i][j-1],    // insertion
                    dp[i-1][j-1]   // substitution
                );
            }
        }
    }
    
    return dp[m][n];
}

const str1 = "kitten";
const str2 = "sitting";
const distance = editDistance(str1, str2);
console.log(`Edit distance between '${str1}' and '${str2}': ${distance}`);
