public class QuickSortTest {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        QuickSort.quickSort(arr, 0, arr.length - 1);
        assert arr[0] == 11 && arr[6] == 90 : "Quick sort failed";
        System.out.println("QuickSortTest passed");
    }
}
