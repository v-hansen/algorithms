public class TwoPointersTest {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = TwoPointers.twoSum(arr, 9);
        assert result[0] == 3 && result[1] == 4 : "Two pointers failed";
        System.out.println("TwoPointersTest passed");
    }
}
