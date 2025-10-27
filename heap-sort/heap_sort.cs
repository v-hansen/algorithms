using System;

class HeapSort {
    static void Heapify(int[] arr, int n, int i) {
        int largest = i, left = 2*i+1, right = 2*i+2;
        if (left < n && arr[left] > arr[largest]) largest = left;
        if (right < n && arr[right] > arr[largest]) largest = right;
        if (largest != i) {
            int temp = arr[i]; arr[i] = arr[largest]; arr[largest] = temp;
            Heapify(arr, n, largest);
        }
    }
    
    static void Sort(int[] arr) {
        int n = arr.Length;
        for (int i = n/2-1; i >= 0; i--) Heapify(arr, n, i);
        for (int i = n-1; i > 0; i--) {
            int temp = arr[0]; arr[0] = arr[i]; arr[i] = temp;
            Heapify(arr, i, 0);
        }
    }
    
    static void Main() {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        Sort(arr);
        Console.WriteLine(string.Join(" ", arr));
    }
}