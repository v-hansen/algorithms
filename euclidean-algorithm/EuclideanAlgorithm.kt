fun gcd(a: Int, b: Int): Int {
    var x = a
    var y = b
    while (y != 0) {
        val temp = y
        y = x % y
        x = temp
    }
    return x
}

fun gcdRecursive(a: Int, b: Int): Int {
    return if (b == 0) a else gcdRecursive(b, a % b)
}

fun lcm(a: Int, b: Int): Int {
    return (a * b) / gcd(a, b)
}

fun extendedGcd(a: Int, b: Int): Triple<Int, Int, Int> {
    if (b == 0) {
        return Triple(a, 1, 0)
    }
    val (gcd, x1, y1) = extendedGcd(b, a % b)
    val x = y1
    val y = x1 - (a / b) * y1
    return Triple(gcd, x, y)
}

fun main() {
    println("GCD: ${gcd(48, 18)}")
    println("GCD recursive: ${gcdRecursive(48, 18)}")
    println("LCM: ${lcm(48, 18)}")
    
    val (gcd, x, y) = extendedGcd(48, 18)
    println("Extended GCD: gcd=$gcd, x=$x, y=$y")
}