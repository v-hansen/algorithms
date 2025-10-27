def sieve_of_eratosthenes(n)
  primes = Array.new(n + 1, true)
  primes[0] = primes[1] = false
  
  (2..Math.sqrt(n)).each do |i|
    if primes[i]
      (i * i).step(n, i) { |j| primes[j] = false }
    end
  end
  
  (2..n).select { |i| primes[i] }
end

puts sieve_of_eratosthenes(30).inspect