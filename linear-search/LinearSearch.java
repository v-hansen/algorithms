public class LinearSearch {
    public static int search(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    public static int searchRecursive(int[] arr, int target, int index) {
        if (index >= arr.length) return -1;
        if (arr[index] == target) return index;
        return searchRecursive(arr, target, index + 1);
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("Iterative: " + search(arr, 3));
        System.out.println("Recursive: " + searchRecursive(arr, 3, 0));
    }
}