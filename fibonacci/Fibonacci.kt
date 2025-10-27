fun fibonacci(n: Int): Long {
    return when {
        n <= 1 -> n.toLong()
        else -> {
            var a = 0L
            var b = 1L
            repeat(n - 1) {
                val temp = a + b
                a = b
                b = temp
            }
            b
        }
    }
}

fun fibonacciSequence(count: Int): List<Long> {
    return (0 until count).map { fibonacci(it) }
}

fun main() {
    println("Sequência de Fibonacci:")
    fibonacciSequence(15).forEachIndexed { index, value ->
        println("F($index) = $value")
    }
    
    println("\nTeste com número específico:")
    println("F(20) = ${fibonacci(20)}")
}