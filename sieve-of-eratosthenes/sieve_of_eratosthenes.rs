fn sieve_of_eratosthenes(n: usize) -> Vec<usize> {
    let mut is_prime = vec![true; n + 1];
    is_prime[0] = false;
    if n > 0 { is_prime[1] = false; }
    
    let mut p = 2;
    while p * p <= n {
        if is_prime[p] {
            let mut i = p * p;
            while i <= n {
                is_prime[i] = false;
                i += p;
            }
        }
        p += 1;
    }
    
    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn count_primes(n: usize) -> usize {
    if n < 2 { return 0; }
    
    let mut is_prime = vec![true; n];
    is_prime[0] = false;
    if n > 1 { is_prime[1] = false; }
    
    let mut p = 2;
    while p * p < n {
        if is_prime[p] {
            let mut i = p * p;
            while i < n {
                is_prime[i] = false;
                i += p;
            }
        }
        p += 1;
    }
    
    is_prime.iter().filter(|&&x| x).count()
}

fn main() {
    let primes = sieve_of_eratosthenes(30);
    println!("Primes up to 30: {:?}", primes);
    println!("Count of primes up to 30: {}", count_primes(30));
}