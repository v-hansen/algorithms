fun linearSearch(arr: IntArray, target: Int): Int {
    return arr.indexOf(target)
}

fun linearSearchManual(arr: IntArray, target: Int): Int {
    for (i in arr.indices) {
        if (arr[i] == target) return i
    }
    return -1
}

fun linearSearchRecursive(arr: IntArray, target: Int, index: Int = 0): Int {
    if (index >= arr.size) return -1
    if (arr[index] == target) return index
    return linearSearchRecursive(arr, target, index + 1)
}

fun main() {
    val arr = intArrayOf(1, 2, 3, 4, 5)
    println("Built-in: ${linearSearch(arr, 3)}")
    println("Manual: ${linearSearchManual(arr, 3)}")
    println("Recursive: ${linearSearchRecursive(arr, 3)}")
}