(defn binary-search [arr target]
  (loop [left 0 right (dec (count arr))]
    (if (<= left right)
      (let [mid (+ left (quot (- right left) 2))]
        (cond
          (= (nth arr mid) target) mid
          (< (nth arr mid) target) (recur (inc mid) right)
          :else (recur left (dec mid))))
      -1)))

(def arr [1 3 5 7 9 11])
(println (binary-search arr 7))
(println (binary-search arr 4))
