fun lcs(X: String, Y: String): Int {
    val m = X.length
    val n = Y.length
    val L = Array(m + 1) { IntArray(n + 1) }
    
    for (i in 0..m) {
        for (j in 0..n) {
            when {
                i == 0 || j == 0 -> L[i][j] = 0
                X[i-1] == Y[j-1] -> L[i][j] = L[i-1][j-1] + 1
                else -> L[i][j] = maxOf(L[i-1][j], L[i][j-1])
            }
        }
    }
    
    return L[m][n]
}

fun main() {
    println(lcs("ABCDGH", "AEDFHR"))
}
