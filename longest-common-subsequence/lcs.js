function lcsLength(text1, text2) {
    const m = text1.length;
    const n = text2.length;
    const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));
    
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i-1] === text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    return dp[m][n];
}

function lcsString(text1, text2) {
    const m = text1.length;
    const n = text2.length;
    const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));
    
    // Fill DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i-1] === text2[j-1]) {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    
    // Backtrack to find LCS
    const lcs = [];
    let i = m, j = n;
    while (i > 0 && j > 0) {
        if (text1[i-1] === text2[j-1]) {
            lcs.push(text1[i-1]);
            i--;
            j--;
        } else if (dp[i-1][j] > dp[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }
    
    return lcs.reverse().join('');
}

// Test
const text1 = "ABCDGH";
const text2 = "AEDFHR";
console.log(`LCS length: ${lcsLength(text1, text2)}`); // 3
console.log(`LCS string: ${lcsString(text1, text2)}`); // ADH
