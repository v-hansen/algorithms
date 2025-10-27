#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

void sieveOfEratosthenes(int n) {
    bool *prime = malloc((n + 1) * sizeof(bool));
    for (int i = 0; i <= n; i++) prime[i] = true;
    
    prime[0] = prime[1] = false;
    
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }
    
    printf("Primes up to %d: ", n);
    for (int i = 2; i <= n; i++) {
        if (prime[i]) printf("%d ", i);
    }
    printf("\n");
    
    free(prime);
}

int main() {
    sieveOfEratosthenes(30);
    return 0;
}