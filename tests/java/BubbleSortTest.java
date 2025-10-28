public class BubbleSortTest {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        BubbleSort.bubbleSort(arr);
        assert arr[0] == 11 && arr[6] == 90 : "Bubble sort failed";
        System.out.println("BubbleSortTest passed");
    }
}
