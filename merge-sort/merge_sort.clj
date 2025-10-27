(defn merge-arrays [left right]
  (loop [result [] l left r right]
    (cond
      (empty? l) (concat result r)
      (empty? r) (concat result l)
      (<= (first l) (first r)) (recur (conj result (first l)) (rest l) r)
      :else (recur (conj result (first r)) l (rest r)))))

(defn merge-sort [arr]
  (if (<= (count arr) 1)
    arr
    (let [mid (quot (count arr) 2)
          left (merge-sort (take mid arr))
          right (merge-sort (drop mid arr))]
      (merge-arrays left right))))

(println (merge-sort [64 34 25 12 22 11 90]))
