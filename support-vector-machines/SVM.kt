class SVM(
    private val lr: Double = 0.001,
    private val lambdaParam: Double = 0.01,
    private val nIters: Int = 1000
) {
    private lateinit var w: DoubleArray
    private var b: Double = 0.0
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        // Convert labels to -1 and 1
        val y_ = y.map { if (it <= 0) -1 else 1 }.toIntArray()
        
        val nFeatures = X[0].size
        w = DoubleArray(nFeatures)
        b = 0.0
        
        repeat(nIters) {
            for (i in X.indices) {
                val xi = X[i]
                val yi = y_[i]
                
                val condition = yi * (dotProduct(xi, w) - b) >= 1
                
                if (condition) {
                    for (j in w.indices) {
                        w[j] -= lr * (2 * lambdaParam * w[j])
                    }
                } else {
                    for (j in w.indices) {
                        w[j] -= lr * (2 * lambdaParam * w[j] - xi[j] * yi)
                    }
                    b -= lr * yi
                }
            }
        }
    }
    
    private fun dotProduct(a: DoubleArray, b: DoubleArray): Double {
        return a.mapIndexed { i, value -> value * b[i] }.sum()
    }
    
    fun predict(X: Array<DoubleArray>): IntArray {
        return X.map { x ->
            val approx = dotProduct(x, w) - b
            val sign = if (approx >= 0) 1 else -1
            (sign + 1) / 2 // Convert back to 0,1
        }.toIntArray()
    }
}

fun main() {
    val X = arrayOf(
        doubleArrayOf(1.0, 2.0), doubleArrayOf(2.0, 3.0), doubleArrayOf(3.0, 1.0),
        doubleArrayOf(6.0, 5.0), doubleArrayOf(7.0, 7.0), doubleArrayOf(8.0, 6.0)
    )
    val y = intArrayOf(0, 0, 0, 1, 1, 1)
    
    val model = SVM()
    model.fit(X, y)
    val predictions = model.predict(arrayOf(doubleArrayOf(2.0, 2.0), doubleArrayOf(7.0, 6.0)))
    println(predictions.contentToString()) // [0, 1]
}
