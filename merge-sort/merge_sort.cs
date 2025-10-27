using System;
using System.Linq;

class MergeSort {
    static int[] Sort(int[] arr) {
        if (arr.Length <= 1) return arr;
        
        int mid = arr.Length / 2;
        var left = Sort(arr.Take(mid).ToArray());
        var right = Sort(arr.Skip(mid).ToArray());
        
        return Merge(left, right);
    }
    
    static int[] Merge(int[] left, int[] right) {
        var result = new int[left.Length + right.Length];
        int i = 0, j = 0, k = 0;
        
        while (i < left.Length && j < right.Length) {
            if (left[i] <= right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }
        
        while (i < left.Length) result[k++] = left[i++];
        while (j < right.Length) result[k++] = right[j++];
        
        return result;
    }
    
    static void Main() {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        Console.WriteLine(string.Join(" ", Sort(arr)));
    }
}
