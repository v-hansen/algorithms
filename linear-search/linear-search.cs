using System;

class Program {
    static int LinearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    static void Main() {
        int[] arr = {5, 2, 8, 1, 9, 3};
        Console.WriteLine(LinearSearch(arr, 8));
        Console.WriteLine(LinearSearch(arr, 7));
    }
}
