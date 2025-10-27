fun fibonacci(n: Int): Int {
    if (n <= 1) return n
    val dp = IntArray(n + 1)
    dp[0] = 0
    dp[1] = 1
    for (i in 2..n) {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return dp[n]
}

fun coinChange(coins: IntArray, amount: Int): Int {
    val dp = IntArray(amount + 1) { Int.MAX_VALUE }
    dp[0] = 0
    
    for (coin in coins) {
        for (i in coin..amount) {
            if (dp[i - coin] != Int.MAX_VALUE) {
                dp[i] = minOf(dp[i], dp[i - coin] + 1)
            }
        }
    }
    
    return if (dp[amount] == Int.MAX_VALUE) -1 else dp[amount]
}

fun main() {
    println("Fibonacci(10): ${fibonacci(10)}")
    println("Coin change: ${coinChange(intArrayOf(1, 3, 4), 6)}")
}