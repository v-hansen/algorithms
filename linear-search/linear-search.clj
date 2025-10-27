(defn linear-search [arr target]
  (loop [i 0]
    (cond
      (>= i (count arr)) -1
      (= (nth arr i) target) i
      :else (recur (inc i)))))

(defn linear-search-recursive [arr target index]
  (cond
    (>= index (count arr)) -1
    (= (nth arr index) target) index
    :else (linear-search-recursive arr target (inc index))))

(println (linear-search [1 2 3 4 5] 3))
(println (linear-search-recursive [1 2 3 4 5] 3 0))