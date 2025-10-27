(defn coin-change [coins amount]
  (let [dp (vec (concat [0] (repeat amount Double/POSITIVE_INFINITY)))]
    (reduce (fn [dp coin]
             (reduce (fn [dp i]
                      (assoc dp i (min (nth dp i) (+ (nth dp (- i coin)) 1))))
                    dp (range coin (inc amount))))
           dp coins)
    (let [result (nth dp amount)]
      (if (= result Double/POSITIVE_INFINITY) -1 result))))

(println (coin-change [1 3 4] 6))