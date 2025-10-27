#include <iostream>
#include <vector>
using namespace std;

vector<int> sieveOfEratosthenes(int n) {
    if (n < 2) return {};
    
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int p = 2; p * p <= n; p++) {
        if (isPrime[p]) {
            for (int i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
    }
    
    vector<int> primes;
    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }
    
    return primes;
}

int main() {
    int n = 30;
    vector<int> primes = sieveOfEratosthenes(n);
    
    cout << "Primes up to " << n << ": ";
    for (int prime : primes) {
        cout << prime << " ";
    }
    cout << endl;
    
    return 0;
}
