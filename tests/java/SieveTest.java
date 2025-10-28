import java.util.*;

public class SieveTest {
    public static void main(String[] args) {
        List<Integer> primes = SieveOfEratosthenes.sieve(30);
        assert primes.contains(2) && primes.contains(29) : "Sieve failed";
        System.out.println("SieveTest passed");
    }
}
