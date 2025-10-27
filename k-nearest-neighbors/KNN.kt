import kotlin.math.*

class KNN(private val k: Int = 3) {
    private lateinit var X_train: Array<DoubleArray>
    private lateinit var y_train: IntArray
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        X_train = X
        y_train = y
    }
    
    private fun euclideanDistance(x1: DoubleArray, x2: DoubleArray): Double {
        return sqrt(x1.mapIndexed { i, x -> (x - x2[i]).pow(2) }.sum())
    }
    
    fun predict(X: Array<DoubleArray>): IntArray {
        return X.map { x ->
            val distances = X_train.mapIndexed { i, x_train ->
                euclideanDistance(x, x_train) to y_train[i]
            }.sortedBy { it.first }
            
            val kNearest = distances.take(k)
            val counts = kNearest.groupBy { it.second }.mapValues { it.value.size }
            counts.maxByOrNull { it.value }?.key ?: 0
        }.toIntArray()
    }
}

fun main() {
    val X_train = arrayOf(
        doubleArrayOf(1.0, 2.0), doubleArrayOf(2.0, 3.0), doubleArrayOf(3.0, 1.0),
        doubleArrayOf(6.0, 5.0), doubleArrayOf(7.0, 7.0), doubleArrayOf(8.0, 6.0)
    )
    val y_train = intArrayOf(0, 0, 0, 1, 1, 1)
    val X_test = arrayOf(doubleArrayOf(2.0, 2.0), doubleArrayOf(7.0, 6.0))
    
    val model = KNN(3)
    model.fit(X_train, y_train)
    println(model.predict(X_test).contentToString()) // [0, 1]
}
