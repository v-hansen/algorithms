fun mergeSort(arr: IntArray): IntArray {
    if (arr.size <= 1) return arr
    
    val mid = arr.size / 2
    val left = mergeSort(arr.sliceArray(0 until mid))
    val right = mergeSort(arr.sliceArray(mid until arr.size))
    
    return merge(left, right)
}

fun merge(left: IntArray, right: IntArray): IntArray {
    val result = IntArray(left.size + right.size)
    var i = 0
    var j = 0
    var k = 0
    
    while (i < left.size && j < right.size) {
        if (left[i] <= right[j]) {
            result[k++] = left[i++]
        } else {
            result[k++] = right[j++]
        }
    }
    
    while (i < left.size) result[k++] = left[i++]
    while (j < right.size) result[k++] = right[j++]
    
    return result
}

fun main() {
    val arr = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    println(mergeSort(arr).contentToString())
}
