function sieveOfEratosthenes(n) {
    if (n < 2) return [];
    
    // Create boolean array and initialize all entries as true
    const isPrime = new Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    
    for (let p = 2; p * p <= n; p++) {
        if (isPrime[p]) {
            // Mark all multiples of p as not prime
            for (let i = p * p; i <= n; i += p) {
                isPrime[i] = false;
            }
        }
    }
    
    // Collect all prime numbers
    const primes = [];
    for (let i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push(i);
        }
    }
    
    return primes;
}

function sieveOptimized(n) {
    if (n < 2) return [];
    if (n === 2) return [2];
    
    // Only consider odd numbers
    const size = Math.floor((n - 1) / 2);
    const isPrime = new Array(size).fill(true);
    
    // Start with 3 and increment by 2
    for (let i = 1; i <= Math.floor((Math.sqrt(n) - 1) / 2); i++) {
        if (isPrime[i]) {
            const p = 2 * i + 1;
            // Mark multiples starting from p^2
            const start = Math.floor((p * p - 1) / 2);
            for (let j = start; j < size; j += p) {
                isPrime[j] = false;
            }
        }
    }
    
    // Collect primes
    const primes = [2];
    for (let i = 0; i < size; i++) {
        if (isPrime[i]) {
            primes.push(2 * i + 1);
        }
    }
    
    return primes;
}

function countPrimes(n) {
    if (n < 2) return 0;
    
    const isPrime = new Array(n).fill(true);
    isPrime[0] = isPrime[1] = false;
    
    for (let i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    return isPrime.filter(Boolean).length;
}

// Test
const n = 30;
const primes = sieveOfEratosthenes(n);
console.log(`Primes up to ${n}: ${primes}`); // [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
console.log(`Count of primes less than ${n}: ${countPrimes(n)}`); // 10
