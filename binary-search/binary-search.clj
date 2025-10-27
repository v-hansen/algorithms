(defn binary-search [arr target]
  (loop [left 0 right (dec (count arr))]
    (when (<= left right)
      (let [mid (quot (+ left right) 2)]
        (cond
          (= (nth arr mid) target) mid
          (< (nth arr mid) target) (recur (inc mid) right)
          :else (recur left (dec mid)))))))

(println (binary-search [1 2 3 4 5] 3))