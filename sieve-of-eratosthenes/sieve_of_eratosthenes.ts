function sieveOfEratosthenes(n: number): number[] {
    const primes = new Array(n + 1).fill(true);
    primes[0] = primes[1] = false;
    
    for (let i = 2; i * i <= n; i++) {
        if (primes[i]) {
            for (let j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }
    
    return primes.map((isPrime, index) => isPrime ? index : -1).filter(x => x !== -1);
}

console.log(sieveOfEratosthenes(30));