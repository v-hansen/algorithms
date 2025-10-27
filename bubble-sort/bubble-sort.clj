(defn bubble-sort [arr]
  (loop [arr arr n (count arr)]
    (if (<= n 1)
      arr
      (let [[new-arr swapped] 
            (reduce (fn [[acc swapped] i]
                     (if (and (< (inc i) (count acc))
                             (> (nth acc i) (nth acc (inc i))))
                       [(assoc acc i (nth acc (inc i)) (inc i) (nth acc i)) true]
                       [acc swapped]))
                   [arr false] (range (dec n)))]
        (if swapped
          (recur new-arr (dec n))
          new-arr)))))

(println (bubble-sort [64 34 25 12 22 11 90]))