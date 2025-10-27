fun matrixMultiply(a: Array<IntArray>, b: Array<IntArray>): Array<IntArray> {
    val rowsA = a.size
    val colsA = a[0].size
    val colsB = b[0].size
    
    val result = Array(rowsA) { IntArray(colsB) }
    
    for (i in 0 until rowsA) {
        for (j in 0 until colsB) {
            for (k in 0 until colsA) {
                result[i][j] += a[i][k] * b[k][j]
            }
        }
    }
    
    return result
}

fun main() {
    val a = arrayOf(intArrayOf(1, 2), intArrayOf(3, 4))
    val b = arrayOf(intArrayOf(5, 6), intArrayOf(7, 8))
    
    val result = matrixMultiply(a, b)
    result.forEach { row ->
        println(row.joinToString(" "))
    }
}
