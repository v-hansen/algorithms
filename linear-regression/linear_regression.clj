(defn linear-regression [X y]
  (let [X-mean (/ (reduce + X) (count X))
        y-mean (/ (reduce + y) (count y))
        num (reduce + (map #(* (- %1 X-mean) (- %2 y-mean)) X y))
        den (reduce + (map #(* (- % X-mean) (- % X-mean)) X))
        w (/ num den)
        b (- y-mean (* w X-mean))]
    {:w w :b b}))

(defn predict [model x]
  (+ (* (:w model) x) (:b model)))

(let [model (linear-regression [1 2 3 4 5] [2 4 6 8 10])]
  (println (predict model 6))) ; 12.0
