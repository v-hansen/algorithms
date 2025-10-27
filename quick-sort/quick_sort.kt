fun quickSort(arr: IntArray, low: Int = 0, high: Int = arr.size - 1) {
    if (low < high) {
        val pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    }
}

fun partition(arr: IntArray, low: Int, high: Int): Int {
    val pivot = arr[high]
    var i = low - 1
    
    for (j in low until high) {
        if (arr[j] <= pivot) {
            i++
            val temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        }
    }
    
    val temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    
    return i + 1
}

fun main() {
    val arr = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    quickSort(arr)
    println(arr.contentToString())
}
