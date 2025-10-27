fun twoSum(arr: IntArray, target: Int): IntArray {
    var left = 0
    var right = arr.size - 1
    while (left < right) {
        val sum = arr[left] + arr[right]
        when {
            sum == target -> return intArrayOf(left, right)
            sum < target -> left++
            else -> right--
        }
    }
    return intArrayOf()
}

fun main() {
    val result = twoSum(intArrayOf(1, 2, 3, 4, 6), 6)
    println("[${result[0]}, ${result[1]}]")
}
