import java.util.*;

public class SieveOfEratosthenes {
    
    public static List<Integer> sieveOfEratosthenes(int n) {
        if (n < 2) return new ArrayList<>();
        
        // Create boolean array and initialize all entries as true
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        
        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                // Mark all multiples of p as not prime
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        
        // Collect all prime numbers
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }
        
        return primes;
    }
    
    public static List<Integer> sieveOptimized(int n) {
        if (n < 2) return new ArrayList<>();
        if (n == 2) return Arrays.asList(2);
        
        // Only consider odd numbers
        int size = (n - 1) / 2;
        boolean[] isPrime = new boolean[size];
        Arrays.fill(isPrime, true);
        
        // Start with 3 and increment by 2
        for (int i = 1; i <= (int)((Math.sqrt(n) - 1) / 2); i++) {
            if (isPrime[i]) {
                int p = 2 * i + 1;
                // Mark multiples starting from p^2
                int start = (p * p - 1) / 2;
                for (int j = start; j < size; j += p) {
                    isPrime[j] = false;
                }
            }
        }
        
        // Collect primes
        List<Integer> primes = new ArrayList<>();
        primes.add(2);
        for (int i = 0; i < size; i++) {
            if (isPrime[i]) {
                primes.add(2 * i + 1);
            }
        }
        
        return primes;
    }
    
    public static int countPrimes(int n) {
        if (n < 2) return 0;
        
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        int count = 0;
        for (boolean prime : isPrime) {
            if (prime) count++;
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        int n = 30;
        List<Integer> primes = sieveOfEratosthenes(n);
        System.out.println("Primes up to " + n + ": " + primes); // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        System.out.println("Count of primes less than " + n + ": " + countPrimes(n)); // 10
    }
}
