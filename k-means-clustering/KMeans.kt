import kotlin.math.*
import kotlin.random.Random

class KMeans(private val k: Int = 3, private val maxIters: Int = 100) {
    private lateinit var centroids: Array<DoubleArray>
    
    fun fit(X: Array<DoubleArray>): IntArray {
        centroids = Array(k) { X[Random.nextInt(X.size)].clone() }
        
        repeat(maxIters) {
            val labels = X.map { point ->
                centroids.indices.minByOrNull { i ->
                    point.mapIndexed { j, x -> (x - centroids[i][j]).pow(2) }.sum()
                } ?: 0
            }.toIntArray()
            
            val newCentroids = Array(k) { DoubleArray(X[0].size) }
            val counts = IntArray(k)
            
            X.forEachIndexed { i, point ->
                val label = labels[i]
                point.forEachIndexed { j, x ->
                    newCentroids[label][j] += x
                }
                counts[label]++
            }
            
            for (i in 0 until k) {
                if (counts[i] > 0) {
                    for (j in newCentroids[i].indices) {
                        newCentroids[i][j] /= counts[i]
                    }
                }
            }
            centroids = newCentroids
        }
        
        return X.map { point ->
            centroids.indices.minByOrNull { i ->
                point.mapIndexed { j, x -> (x - centroids[i][j]).pow(2) }.sum()
            } ?: 0
        }.toIntArray()
    }
}

fun main() {
    val X = arrayOf(doubleArrayOf(1.0, 2.0), doubleArrayOf(1.0, 4.0), doubleArrayOf(1.0, 0.0), 
                   doubleArrayOf(10.0, 2.0), doubleArrayOf(10.0, 4.0), doubleArrayOf(10.0, 0.0))
    val kmeans = KMeans(2)
    println(kmeans.fit(X).contentToString())
}
