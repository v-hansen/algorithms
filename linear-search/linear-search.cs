using System;

class LinearSearch {
    static int Search(int[] arr, int target) {
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    static void Main() {
        int[] arr = {1, 2, 3, 4, 5};
        Console.WriteLine(Search(arr, 3));
    }
}