using System;

class Program {
    static int BinarySearch(int[] arr, int target) {
        int left = 0, right = arr.Length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
    
    static void Main() {
        int[] arr = {1, 3, 5, 7, 9, 11};
        Console.WriteLine(BinarySearch(arr, 7));
        Console.WriteLine(BinarySearch(arr, 4));
    }
}
