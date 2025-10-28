public class KnapsackTest {
    public static void main(String[] args) {
        int[] weights = {1, 2, 3};
        int[] values = {10, 15, 40};
        assert KnapsackProblem.knapsack01(weights, values, 6) == 65 : "Knapsack failed";
        System.out.println("KnapsackTest passed");
    }
}
