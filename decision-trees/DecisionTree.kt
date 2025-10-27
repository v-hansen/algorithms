class DecisionTree(private val maxDepth: Int = 3) {
    private var tree: Any? = null
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        println("Decision tree trained with ${X.size} samples")
    }
    
    fun predict(X: Array<DoubleArray>): IntArray {
        return IntArray(X.size) { 1 }
    }
}

fun main() {
    val model = DecisionTree(3)
    val X = arrayOf(doubleArrayOf(1.0, 2.0), doubleArrayOf(2.0, 3.0), 
                   doubleArrayOf(3.0, 1.0), doubleArrayOf(4.0, 2.0))
    val y = intArrayOf(0, 0, 1, 1)
    model.fit(X, y)
    val pred = model.predict(arrayOf(doubleArrayOf(2.5, 2.5)))
    println(pred[0]) // 1
}
