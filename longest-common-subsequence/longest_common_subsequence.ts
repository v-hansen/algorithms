function lcs(X: string, Y: string): number {
    const m = X.length;
    const n = Y.length;
    const L = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));
    
    for (let i = 0; i <= m; i++) {
        for (let j = 0; j <= n; j++) {
            if (i === 0 || j === 0) {
                L[i][j] = 0;
            } else if (X[i-1] === Y[j-1]) {
                L[i][j] = L[i-1][j-1] + 1;
            } else {
                L[i][j] = Math.max(L[i-1][j], L[i][j-1]);
            }
        }
    }
    
    return L[m][n];
}

console.log(lcs("ABCDGH", "AEDFHR"));