#!/usr/bin/env python3
import os

def complete_euclidean_algorithm():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/euclidean-algorithm"
    
    # Ruby
    with open(f"{base_dir}/euclidean_algorithm.rb", "w") as f:
        f.write("""def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

puts gcd(48, 18)""")

    # Clojure
    with open(f"{base_dir}/euclidean_algorithm.clj", "w") as f:
        f.write("""(defn gcd [a b]
  (if (zero? b) a (recur b (mod a b))))

(println (gcd 48 18))""")

    # TypeScript
    with open(f"{base_dir}/euclidean_algorithm.ts", "w") as f:
        f.write("""function gcd(a: number, b: number): number {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

console.log(gcd(48, 18));""")

def complete_sieve_of_eratosthenes():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/sieve-of-eratosthenes"
    
    # Ruby
    with open(f"{base_dir}/sieve_of_eratosthenes.rb", "w") as f:
        f.write("""def sieve_of_eratosthenes(n)
  primes = Array.new(n + 1, true)
  primes[0] = primes[1] = false
  
  (2..Math.sqrt(n)).each do |i|
    if primes[i]
      (i * i).step(n, i) { |j| primes[j] = false }
    end
  end
  
  (2..n).select { |i| primes[i] }
end

puts sieve_of_eratosthenes(30).inspect""")

    # Clojure
    with open(f"{base_dir}/sieve_of_eratosthenes.clj", "w") as f:
        f.write("""(defn sieve-of-eratosthenes [n]
  (loop [primes (vec (concat [false false] (repeat (- n 1) true)))
         i 2]
    (cond
      (> (* i i) n) (keep-indexed #(when %2 %1) primes)
      (nth primes i) (recur (reduce #(assoc %1 %2 false) primes (range (* i i) (inc n) i)) (inc i))
      :else (recur primes (inc i)))))

(println (sieve-of-eratosthenes 30))""")

    # TypeScript
    with open(f"{base_dir}/sieve_of_eratosthenes.ts", "w") as f:
        f.write("""function sieveOfEratosthenes(n: number): number[] {
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

console.log(sieveOfEratosthenes(30));""")

def complete_matrix_multiplication():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/matrix-multiplication"
    
    # Ruby
    with open(f"{base_dir}/matrix_multiplication.rb", "w") as f:
        f.write("""def matrix_multiply(a, b)
  rows_a, cols_a = a.length, a[0].length
  rows_b, cols_b = b.length, b[0].length
  
  return nil if cols_a != rows_b
  
  result = Array.new(rows_a) { Array.new(cols_b, 0) }
  
  (0...rows_a).each do |i|
    (0...cols_b).each do |j|
      (0...cols_a).each do |k|
        result[i][j] += a[i][k] * b[k][j]
      end
    end
  end
  
  result
end

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
puts matrix_multiply(a, b).inspect""")

    # Clojure
    with open(f"{base_dir}/matrix_multiplication.clj", "w") as f:
        f.write("""(defn matrix-multiply [a b]
  (let [rows-a (count a)
        cols-a (count (first a))
        rows-b (count b)
        cols-b (count (first b))]
    (when (= cols-a rows-b)
      (for [i (range rows-a)]
        (for [j (range cols-b)]
          (reduce + (for [k (range cols-a)]
                     (* (get-in a [i k]) (get-in b [k j])))))))))

(def a [[1 2] [3 4]])
(def b [[5 6] [7 8]])
(println (matrix-multiply a b))""")

    # TypeScript
    with open(f"{base_dir}/matrix_multiplication.ts", "w") as f:
        f.write("""function matrixMultiply(a: number[][], b: number[][]): number[][] | null {
    const rowsA = a.length, colsA = a[0].length;
    const rowsB = b.length, colsB = b[0].length;
    
    if (colsA !== rowsB) return null;
    
    const result: number[][] = Array(rowsA).fill(0).map(() => Array(colsB).fill(0));
    
    for (let i = 0; i < rowsA; i++) {
        for (let j = 0; j < colsB; j++) {
            for (let k = 0; k < colsA; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    
    return result;
}

const a = [[1, 2], [3, 4]];
const b = [[5, 6], [7, 8]];
console.log(matrixMultiply(a, b));""")

def complete_palindrome():
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/palindrome"
    
    # Expandir implementações pequenas
    with open(f"{base_dir}/palindrome.py", "w") as f:
        f.write("""def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_palindrome_two_pointers(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome_two_pointers("race a car"))""")

if __name__ == "__main__":
    print("Completando algoritmos matemáticos...")
    complete_euclidean_algorithm()
    complete_sieve_of_eratosthenes()
    complete_matrix_multiplication()
    complete_palindrome()
    print("Algoritmos matemáticos completados!")
