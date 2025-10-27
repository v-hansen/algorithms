import kotlin.math.*

class LogisticRegression(private val lr: Double = 0.01, private val maxIters: Int = 1000) {
    private lateinit var w: DoubleArray
    private var b: Double = 0.0
    
    private fun sigmoid(z: Double): Double = 1.0 / (1.0 + exp(-z.coerceIn(-500.0, 500.0)))
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        w = DoubleArray(X[0].size)
        b = 0.0
        
        repeat(maxIters) {
            val dw = DoubleArray(w.size)
            var db = 0.0
            
            for (i in X.indices) {
                val z = X[i].mapIndexed { j, x -> x * w[j] }.sum() + b
                val h = sigmoid(z)
                val error = h - y[i]
                
                for (j in w.indices) dw[j] += error * X[i][j]
                db += error
            }
            
            for (j in w.indices) w[j] -= lr * dw[j] / X.size
            b -= lr * db / X.size
        }
    }
    
    fun predict(x: DoubleArray): Int {
        val z = x.mapIndexed { j, xi -> xi * w[j] }.sum() + b
        return if (sigmoid(z) >= 0.5) 1 else 0
    }
}

fun main() {
    val model = LogisticRegression()
    model.fit(arrayOf(doubleArrayOf(1.0,2.0), doubleArrayOf(2.0,3.0), doubleArrayOf(3.0,4.0), doubleArrayOf(4.0,5.0)), intArrayOf(0,0,1,1))
    println(model.predict(doubleArrayOf(2.5, 3.5))) // 1
}
