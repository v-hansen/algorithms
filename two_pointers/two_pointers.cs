using System;

class TwoPointers {
    static int[] TwoSum(int[] arr, int target) {
        int left = 0, right = arr.Length - 1;
        
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return new int[] {left, right};
            else if (sum < target) left++;
            else right--;
        }
        
        return new int[] {};
    }
    
    static void Main() {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = TwoSum(arr, 7);
        if (result.Length > 0) {
            Console.WriteLine($"[{result[0]}, {result[1]}]");
        }
    }
}