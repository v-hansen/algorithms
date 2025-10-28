public class CoinChangeTest {
    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        assert CoinChange.coinChange(coins, 11) == 3 : "Coin change failed";
        System.out.println("CoinChangeTest passed");
    }
}
