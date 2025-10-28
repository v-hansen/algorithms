public class MergeSortTest {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        MergeSort.mergeSort(arr, 0, arr.length - 1);
        assert arr[0] == 11 && arr[6] == 90 : "Merge sort failed";
        System.out.println("MergeSortTest passed");
    }
}
