public class TwoPointers {
    public static int[] twoSum(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return new int[]{left, right};
            if (sum < target) left++; else right--;
        }
        return new int[]{};
    }
    
    public static void main(String[] args) {
        int[] result = twoSum(new int[]{1, 2, 3, 4, 6}, 6);
        System.out.println("[" + result[0] + ", " + result[1] + "]");
    }
}
