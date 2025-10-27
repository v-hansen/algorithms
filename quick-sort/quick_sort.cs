using System;
using System.Linq;

class QuickSort {
    static int[] Sort(int[] arr) {
        if (arr.Length <= 1) return arr;
        
        int pivot = arr[0];
        var less = arr.Skip(1).Where(x => x < pivot).ToArray();
        var greater = arr.Skip(1).Where(x => x >= pivot).ToArray();
        
        return Sort(less).Concat(new[] { pivot }).Concat(Sort(greater)).ToArray();
    }
    
    static void Main() {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        var sorted = Sort(arr);
        Console.WriteLine(string.Join(" ", sorted));
    }
}