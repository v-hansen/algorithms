import kotlin.math.*
import kotlin.random.Random

class SimpleDecisionTree(private val maxDepth: Int = 3) {
    private var feature: Int? = null
    private var threshold: Double? = null
    private var left: Any? = null
    private var right: Any? = null
    
    private fun gini(y: IntArray): Double {
        val counts = y.groupBy { it }.mapValues { it.value.size }
        var impurity = 1.0
        counts.values.forEach { count ->
            val prob = count.toDouble() / y.size
            impurity -= prob * prob
        }
        return impurity
    }
    
    fun fit(X: Array<DoubleArray>, y: IntArray, depth: Int = 0): Any {
        if (depth >= maxDepth || y.distinct().size == 1) {
            return y.groupBy { it }.maxByOrNull { it.value.size }?.key ?: y[0]
        }
        
        var bestGini = Double.POSITIVE_INFINITY
        var bestFeature: Int? = null
        var bestThreshold: Double? = null
        
        // Random feature selection
        val nFeatures = sqrt(X[0].size.toDouble()).toInt()
        val features = (0 until X[0].size).shuffled().take(nFeatures)
        
        for (feature in features) {
            val thresholds = X.map { it[feature] }.distinct()
            for (threshold in thresholds) {
                val leftMask = X.map { it[feature] <= threshold }
                val yLeft = y.filterIndexed { i, _ -> leftMask[i] }.toIntArray()
                val yRight = y.filterIndexed { i, _ -> !leftMask[i] }.toIntArray()
                
                if (yLeft.isEmpty() || yRight.isEmpty()) continue
                
                val gini = (yLeft.size * gini(yLeft) + yRight.size * gini(yRight)) / y.size
                if (gini < bestGini) {
                    bestGini = gini
                    bestFeature = feature
                    bestThreshold = threshold
                }
            }
        }
        
        if (bestFeature == null) {
            return y.groupBy { it }.maxByOrNull { it.value.size }?.key ?: y[0]
        }
        
        val leftMask = X.map { it[bestFeature] <= bestThreshold!! }
        val XLeft = X.filterIndexed { i, _ -> leftMask[i] }.toTypedArray()
        val XRight = X.filterIndexed { i, _ -> !leftMask[i] }.toTypedArray()
        val yLeft = y.filterIndexed { i, _ -> leftMask[i] }.toIntArray()
        val yRight = y.filterIndexed { i, _ -> !leftMask[i] }.toIntArray()
        
        this.feature = bestFeature
        this.threshold = bestThreshold
        this.left = SimpleDecisionTree(maxDepth).fit(XLeft, yLeft, depth + 1)
        this.right = SimpleDecisionTree(maxDepth).fit(XRight, yRight, depth + 1)
        
        return this
    }
    
    fun predictOne(x: DoubleArray): Int {
        if (feature == null) return this as Int
        
        return if (x[feature!!] <= threshold!!) {
            when (left) {
                is SimpleDecisionTree -> left!!.predictOne(x)
                else -> left as Int
            }
        } else {
            when (right) {
                is SimpleDecisionTree -> right!!.predictOne(x)
                else -> right as Int
            }
        }
    }
}

class RandomForest(private val nTrees: Int = 10, private val maxDepth: Int = 3) {
    private val trees = mutableListOf<SimpleDecisionTree>()
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        trees.clear()
        
        repeat(nTrees) {
            // Bootstrap sampling
            val indices = IntArray(X.size) { Random.nextInt(X.size) }
            val XSample = indices.map { X[it] }.toTypedArray()
            val ySample = indices.map { y[it] }.toIntArray()
            
            val tree = SimpleDecisionTree(maxDepth)
            val result = tree.fit(XSample, ySample)
            if (result is SimpleDecisionTree) {
                trees.add(result)
            }
        }
    }
    
    fun predict(X: Array<DoubleArray>): IntArray {
        return X.map { x ->
            val treePredictions = trees.map { it.predictOne(x) }
            treePredictions.groupBy { it }.maxByOrNull { it.value.size }?.key ?: 0
        }.toIntArray()
    }
}

fun main() {
    val X = arrayOf(
        doubleArrayOf(1.0, 2.0), doubleArrayOf(2.0, 3.0), doubleArrayOf(3.0, 1.0),
        doubleArrayOf(6.0, 5.0), doubleArrayOf(7.0, 7.0), doubleArrayOf(8.0, 6.0)
    )
    val y = intArrayOf(0, 0, 0, 1, 1, 1)
    
    val model = RandomForest(5, 3)
    model.fit(X, y)
    val predictions = model.predict(arrayOf(doubleArrayOf(2.0, 2.0), doubleArrayOf(7.0, 6.0)))
    println(predictions.contentToString()) // [0, 1]
}
