(defn sieve-of-eratosthenes [n]
  (loop [primes (vec (concat [false false] (repeat (- n 1) true)))
         i 2]
    (cond
      (> (* i i) n) (keep-indexed #(when %2 %1) primes)
      (nth primes i) (recur (reduce #(assoc %1 %2 false) primes (range (* i i) (inc n) i)) (inc i))
      :else (recur primes (inc i)))))

(println (sieve-of-eratosthenes 30))