import kotlin.math.*

data class Tree(
    val prediction: Double? = null,
    val feature: Int? = null,
    val threshold: Double? = null,
    val leftPred: Double? = null,
    val rightPred: Double? = null
)

class GradientBoosting(
    private val nEstimators: Int = 10,
    private val learningRate: Double = 0.1,
    private val maxDepth: Int = 3
) {
    private val trees = mutableListOf<Tree>()
    private var initialPrediction: Double = 0.0
    
    private fun sigmoid(x: Double): Double {
        return 1.0 / (1.0 + exp(-x.coerceIn(-500.0, 500.0)))
    }
    
    fun fit(X: Array<DoubleArray>, y: IntArray) {
        // Initialize with log odds
        val meanY = y.average()
        initialPrediction = ln(meanY / (1 - meanY))
        
        // Current predictions
        val currentPredictions = DoubleArray(y.size) { initialPrediction }
        
        repeat(nEstimators) {
            // Calculate residuals (negative gradient)
            val probabilities = currentPredictions.map { sigmoid(it) }
            val residuals = y.mapIndexed { i, yi -> yi - probabilities[i] }.toDoubleArray()
            
            // Fit a simple regression tree to residuals
            val tree = fitTree(X, residuals)
            trees.add(tree)
            
            // Update predictions
            val treePredictions = predictTree(X, tree)
            for (j in currentPredictions.indices) {
                currentPredictions[j] += learningRate * treePredictions[j]
            }
        }
    }
    
    private fun fitTree(X: Array<DoubleArray>, y: DoubleArray): Tree {
        var bestMse = Double.POSITIVE_INFINITY
        var bestFeature: Int? = null
        var bestThreshold: Double? = null
        
        for (feature in X[0].indices) {
            val thresholds = X.map { it[feature] }.distinct()
            for (threshold in thresholds) {
                val leftMask = X.map { it[feature] <= threshold }
                val yLeft = y.filterIndexed { i, _ -> leftMask[i] }
                val yRight = y.filterIndexed { i, _ -> !leftMask[i] }
                
                if (yLeft.isEmpty() || yRight.isEmpty()) continue
                
                val leftPred = yLeft.average()
                val rightPred = yRight.average()
                
                val mse = yLeft.sumOf { (it - leftPred).pow(2) } + 
                         yRight.sumOf { (it - rightPred).pow(2) }
                
                if (mse < bestMse) {
                    bestMse = mse
                    bestFeature = feature
                    bestThreshold = threshold
                }
            }
        }
        
        if (bestFeature == null) {
            return Tree(prediction = y.average())
        }
        
        val leftMask = X.map { it[bestFeature] <= bestThreshold!! }
        val yLeft = y.filterIndexed { i, _ -> leftMask[i] }
        val yRight = y.filterIndexed { i, _ -> !leftMask[i] }
        
        val leftPred = if (yLeft.isNotEmpty()) yLeft.average() else 0.0
        val rightPred = if (yRight.isNotEmpty()) yRight.average() else 0.0
        
        return Tree(
            feature = bestFeature,
            threshold = bestThreshold,
            leftPred = leftPred,
            rightPred = rightPred
        )
    }
    
    private fun predictTree(X: Array<DoubleArray>, tree: Tree): DoubleArray {
        if (tree.prediction != null) {
            return DoubleArray(X.size) { tree.prediction }
        }
        
        return X.map { x ->
            if (x[tree.feature!!] <= tree.threshold!!) tree.leftPred!! else tree.rightPred!!
        }.toDoubleArray()
    }
    
    fun predict(X: Array<DoubleArray>): IntArray {
        val predictions = DoubleArray(X.size) { initialPrediction }
        
        for (tree in trees) {
            val treePredictions = predictTree(X, tree)
            for (i in predictions.indices) {
                predictions[i] += learningRate * treePredictions[i]
            }
        }
        
        return predictions.map { prediction ->
            val probability = sigmoid(prediction)
            if (probability >= 0.5) 1 else 0
        }.toIntArray()
    }
}

fun main() {
    val X = arrayOf(
        doubleArrayOf(1.0, 2.0), doubleArrayOf(2.0, 3.0), doubleArrayOf(3.0, 1.0),
        doubleArrayOf(6.0, 5.0), doubleArrayOf(7.0, 7.0), doubleArrayOf(8.0, 6.0)
    )
    val y = intArrayOf(0, 0, 0, 1, 1, 1)
    
    val model = GradientBoosting(5, 0.1, 3)
    model.fit(X, y)
    val predictions = model.predict(arrayOf(doubleArrayOf(2.0, 2.0), doubleArrayOf(7.0, 6.0)))
    println(predictions.contentToString()) // [0, 1]
}
