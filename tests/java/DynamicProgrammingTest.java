public class DynamicProgrammingTest {
    public static void main(String[] args) {
        assert DynamicProgramming.fibonacci(10) == 55 : "DP Fibonacci failed";
        int[] coins = {1, 2, 5};
        assert DynamicProgramming.coinChange(coins, 11) == 3 : "DP Coin change failed";
        System.out.println("DynamicProgrammingTest passed");
    }
}
