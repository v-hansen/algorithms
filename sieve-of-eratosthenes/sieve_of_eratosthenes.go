package main

import "fmt"

func sieveOfEratosthenes(n int) []int {
    if n < 2 {
        return []int{}
    }
    
    isPrime := make([]bool, n+1)
    for i := range isPrime {
        isPrime[i] = true
    }
    isPrime[0] = false
    isPrime[1] = false
    
    for p := 2; p*p <= n; p++ {
        if isPrime[p] {
            for i := p * p; i <= n; i += p {
                isPrime[i] = false
            }
        }
    }
    
    var primes []int
    for i := 2; i <= n; i++ {
        if isPrime[i] {
            primes = append(primes, i)
        }
    }
    
    return primes
}

func main() {
    n := 30
    primes := sieveOfEratosthenes(n)
    fmt.Printf("Primes up to %d: %v\n", n, primes)
}
