fun sieveOfEratosthenes(n: Int): List<Int> {
    val prime = BooleanArray(n + 1) { true }
    prime[0] = false
    if (n > 0) prime[1] = false
    
    var p = 2
    while (p * p <= n) {
        if (prime[p]) {
            var i = p * p
            while (i <= n) {
                prime[i] = false
                i += p
            }
        }
        p++
    }
    
    return (2..n).filter { prime[it] }
}

fun main() {
    println(sieveOfEratosthenes(30))
}