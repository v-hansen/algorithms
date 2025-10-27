fun heapify(arr: IntArray, n: Int, i: Int) {
    var largest = i
    val left = 2 * i + 1
    val right = 2 * i + 2
    
    if (left < n && arr[left] > arr[largest]) largest = left
    if (right < n && arr[right] > arr[largest]) largest = right
    
    if (largest != i) {
        val temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        heapify(arr, n, largest)
    }
}

fun heapSort(arr: IntArray) {
    val n = arr.size
    
    for (i in n / 2 - 1 downTo 0) {
        heapify(arr, n, i)
    }
    
    for (i in n - 1 downTo 1) {
        val temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0)
    }
}

fun main() {
    val arr = intArrayOf(64, 34, 25, 12, 22, 11, 90)
    heapSort(arr)
    println(arr.contentToString())
}