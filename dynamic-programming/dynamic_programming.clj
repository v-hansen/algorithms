(def fib-memo
  (memoize (fn [n]
             (if (<= n 2) 1
                 (+ (fib-memo (- n 1)) (fib-memo (- n 2)))))))

(defn coin-change [coins amount]
  (let [dp (vec (concat [0] (repeat amount Double/POSITIVE_INFINITY)))]
    (loop [dp dp coin-idx 0]
      (if (>= coin-idx (count coins))
        (let [result (nth dp amount)]
          (if (= result Double/POSITIVE_INFINITY) -1 result))
        (let [coin (nth coins coin-idx)
              new-dp (reduce (fn [acc i]
                              (assoc acc i (min (nth acc i) (+ (nth acc (- i coin)) 1))))
                            dp (range coin (inc amount)))]
          (recur new-dp (inc coin-idx)))))))

(println "Fib(10):" (fib-memo 10))
(println "Coin change:" (coin-change [1 3 4] 6))