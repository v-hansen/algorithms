using System;

class TwoPointers {
    static int[] TwoSum(int[] arr, int target) {
        int left = 0, right = arr.Length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return new int[] {left, right};
            if (sum < target) left++; else right--;
        }
        return new int[] {};
    }
    
    static void Main() {
        var result = TwoSum(new int[] {1, 2, 3, 4, 6}, 6);
        Console.WriteLine($"[{result[0]}, {result[1]}]");
    }
}
