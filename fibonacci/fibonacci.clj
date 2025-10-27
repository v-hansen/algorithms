(defn fibonacci [n]
  (cond
    (<= n 1) n
    :else (loop [a 0 b 1 i 2]
            (if (> i n)
              b
              (recur b (+ a b) (inc i))))))

(defn fibonacci-seq [count]
  (map fibonacci (range count)))

(defn fibonacci-lazy []
  (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))

; Exemplo de uso
(println "Sequência de Fibonacci:")
(doseq [[i value] (map-indexed vector (take 15 (fibonacci-lazy)))]
  (println (str "F(" i ") = " value)))

(println (str "\nF(20) = " (fibonacci 20)))

; Versão mais idiomática usando lazy sequence
(println "\nPrimeiros 10 números (lazy):")
(println (take 10 (fibonacci-lazy)))