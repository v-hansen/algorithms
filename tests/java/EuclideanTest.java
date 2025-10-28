public class EuclideanTest {
    public static void main(String[] args) {
        assert EuclideanAlgorithm.gcd(48, 18) == 6 : "Euclidean failed";
        assert EuclideanAlgorithm.gcd(100, 50) == 50 : "Euclidean failed";
        System.out.println("EuclideanTest passed");
    }
}
