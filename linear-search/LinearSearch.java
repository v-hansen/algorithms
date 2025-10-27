public class LinearSearch {
    public static int linearSearch(int[] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) return i;
        }
        return -1;
    }
    
    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 1, 9, 3};
        System.out.println(linearSearch(arr, 8));
        System.out.println(linearSearch(arr, 7));
    }
}
