public class LinearSearchTest {
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22};
        assert LinearSearch.linearSearch(arr, 25) == 2 : "Linear search failed";
        assert LinearSearch.linearSearch(arr, 99) == -1 : "Linear search failed";
        System.out.println("LinearSearchTest passed");
    }
}
