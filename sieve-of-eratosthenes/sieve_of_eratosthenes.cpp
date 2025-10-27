#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> sieveOfEratosthenes(int n) {
    vector<bool> prime(n + 1, true);
    prime[0] = prime[1] = false;
    
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }
    
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (prime[i]) primes.push_back(i);
    }
    
    return primes;
}

vector<int> segmentedSieve(int low, int high) {
    int limit = sqrt(high) + 1;
    vector<int> primes = sieveOfEratosthenes(limit);
    
    vector<bool> isPrime(high - low + 1, true);
    
    for (int prime : primes) {
        int start = max(prime * prime, (low + prime - 1) / prime * prime);
        for (int j = start; j <= high; j += prime) {
            isPrime[j - low] = false;
        }
    }
    
    vector<int> result;
    for (int i = low; i <= high; i++) {
        if (isPrime[i - low] && i > 1) {
            result.push_back(i);
        }
    }
    
    return result;
}

int main() {
    auto primes = sieveOfEratosthenes(30);
    cout << "Primes up to 30: ";
    for (int p : primes) cout << p << " ";
    cout << endl;
    
    auto segPrimes = segmentedSieve(10, 20);
    cout << "Primes from 10 to 20: ";
    for (int p : segPrimes) cout << p << " ";
    cout << endl;
    
    return 0;
}