public class FibonacciTest {
    public static void main(String[] args) {
        assert Fibonacci.fibonacciIterative(10) == 55 : "Fibonacci failed";
        assert Fibonacci.fibonacciIterative(0) == 0 : "Fibonacci failed";
        System.out.println("FibonacciTest passed");
    }
}
