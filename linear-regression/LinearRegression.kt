class LinearRegression {
    private var w: Double = 0.0
    private var b: Double = 0.0
    
    fun fit(X: DoubleArray, y: DoubleArray) {
        val X_mean = X.average()
        val y_mean = y.average()
        
        var num = 0.0
        var den = 0.0
        for (i in X.indices) {
            num += (X[i] - X_mean) * (y[i] - y_mean)
            den += (X[i] - X_mean) * (X[i] - X_mean)
        }
        w = num / den
        b = y_mean - w * X_mean
    }
    
    fun predict(x: Double): Double = w * x + b
}

fun main() {
    val model = LinearRegression()
    model.fit(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0), doubleArrayOf(2.0, 4.0, 6.0, 8.0, 10.0))
    println(model.predict(6.0)) // 12.0
}
