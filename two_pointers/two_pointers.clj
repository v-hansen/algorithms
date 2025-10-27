(defn two-sum [arr target]
  (loop [left 0 right (dec (count arr))]
    (when (< left right)
      (let [sum (+ (nth arr left) (nth arr right))]
        (cond
          (= sum target) [left right]
          (< sum target) (recur (inc left) right)
          :else (recur left (dec right)))))))

(println (two-sum [1 2 3 4 6] 6)) ; [1 3]
