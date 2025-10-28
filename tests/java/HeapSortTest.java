public class HeapSortTest {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        HeapSort.heapSort(arr);
        assert arr[0] == 11 && arr[6] == 90 : "Heap sort failed";
        System.out.println("HeapSortTest passed");
    }
}
