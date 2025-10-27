(defn quick-sort [coll]
  (if (<= (count coll) 1)
    coll
    (let [pivot (first coll)
          rest-coll (rest coll)
          less (filter #(< % pivot) rest-coll)
          greater (filter #(>= % pivot) rest-coll)]
      (concat (quick-sort less) [pivot] (quick-sort greater)))))

(println (quick-sort [64 34 25 12 22 11 90]))