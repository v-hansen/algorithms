(defn linear-search [arr target]
  (loop [i 0]
    (cond
      (>= i (count arr)) -1
      (= (nth arr i) target) i
      :else (recur (inc i)))))

(def arr [5 2 8 1 9 3])
(println (linear-search arr 8))
(println (linear-search arr 7))
