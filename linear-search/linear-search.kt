fun linearSearch(arr: IntArray, target: Int): Int {
    for (i in arr.indices) {
        if (arr[i] == target) return i
    }
    return -1
}

fun main() {
    val arr = intArrayOf(5, 2, 8, 1, 9, 3)
    println(linearSearch(arr, 8))
    println(linearSearch(arr, 7))
}
