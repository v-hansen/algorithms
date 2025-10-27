(defn bubble-sort [arr]
  (let [n (count arr)]
    (loop [arr (vec arr) i 0]
      (if (< i (dec n))
        (recur
          (loop [arr arr j 0]
            (if (< j (- n i 1))
              (if (> (nth arr j) (nth arr (inc j)))
                (recur (assoc arr j (nth arr (inc j)) (inc j) (nth arr j)) (inc j))
                (recur arr (inc j)))
              arr))
          (inc i))
        arr))))

(println (bubble-sort [64 34 25 12 22 11 90]))
