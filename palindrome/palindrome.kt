fun isPalindrome(str: String): Boolean {
    val cleaned = str.lowercase()
    return cleaned == cleaned.reversed()
}

fun main() {
    println(isPalindrome("racecar"))
    println(isPalindrome("hello"))
}
