(defn lcs [str1 str2]
  (let [m (count str1)
        n (count str2)
        dp (vec (for [i (range (inc m))]
                 (vec (repeat (inc n) 0))))]
    (reduce (fn [dp i]
             (reduce (fn [dp j]
                      (if (= (nth str1 (dec i)) (nth str2 (dec j)))
                        (assoc-in dp [i j] (inc (get-in dp [(dec i) (dec j)])))
                        (assoc-in dp [i j] (max (get-in dp [(dec i) j])
                                               (get-in dp [i (dec j)])))))
                    dp (range 1 (inc n))))
           dp (range 1 (inc m)))
    (get-in dp [m n])))

(println (lcs "ABCDGH" "AEDFHR"))