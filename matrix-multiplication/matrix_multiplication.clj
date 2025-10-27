(defn matrix-multiply [a b]
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
(println (matrix-multiply a b))