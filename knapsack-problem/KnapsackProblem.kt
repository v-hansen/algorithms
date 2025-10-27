fun knapsack(weights: IntArray, values: IntArray, capacity: Int): Int {
    val n = weights.size
    val dp = Array(n + 1) { IntArray(capacity + 1) }
    
    for (i in 1..n) {
        for (w in 1..capacity) {
            if (weights[i-1] <= w) {
                dp[i][w] = maxOf(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            } else {
                dp[i][w] = dp[i-1][w]
            }
        }
    }
    
    return dp[n][capacity]
}

fun main() {
    println(knapsack(intArrayOf(2, 1, 3), intArrayOf(4, 2, 3), 4))
}
