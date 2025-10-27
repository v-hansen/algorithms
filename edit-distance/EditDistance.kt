fun editDistance(str1: String, str2: String): Int {
    val m = str1.length
    val n = str2.length
    val dp = Array(m + 1) { IntArray(n + 1) }
    
    for (i in 0..m) dp[i][0] = i
    for (j in 0..n) dp[0][j] = j
    
    for (i in 1..m) {
        for (j in 1..n) {
            dp[i][j] = if (str1[i-1] == str2[j-1]) {
                dp[i-1][j-1]
            } else {
                1 + minOf(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            }
        }
    }
    
    return dp[m][n]
}

fun main() {
    println(editDistance("kitten", "sitting"))
}
