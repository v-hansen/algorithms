def sieve_of_eratosthenes(n):
    """Find all prime numbers up to n using Sieve of Eratosthenes"""
    if n < 2:
        return []
    
    # Create boolean array and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= n:
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def sieve_optimized(n):
    """Optimized version using only odd numbers"""
    if n < 2:
        return []
    if n == 2:
        return [2]
    
    # Only consider odd numbers
    size = (n - 1) // 2
    is_prime = [True] * size
    
    # Start with 3 and increment by 2
    for i in range(1, int((n**0.5 - 1) / 2) + 1):
        if is_prime[i]:
            p = 2 * i + 1
            # Mark multiples starting from p^2
            start = (p * p - 1) // 2
            for j in range(start, size, p):
                is_prime[j] = False
    
    # Collect primes
    primes = [2] + [2 * i + 1 for i in range(size) if is_prime[i]]
    return primes

def count_primes(n):
    """Count number of primes less than n"""
    if n < 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)

# Test
n = 30
primes = sieve_of_eratosthenes(n)
print(f"Primes up to {n}: {primes}")  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(f"Count of primes less than {n}: {count_primes(n)}")  # 10
