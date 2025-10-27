(defn edit-distance [str1 str2]
  (let [m (count str1)
        n (count str2)
        dp (vec (for [i (range (inc m))]
                 (vec (repeat (inc n) 0))))]
    
    (let [dp (reduce (fn [dp i] (assoc-in dp [i 0] i)) dp (range (inc m)))
          dp (reduce (fn [dp j] (assoc-in dp [0 j] j)) dp (range (inc n)))]
      
      (loop [dp dp i 1]
        (if (> i m)
          (get-in dp [m n])
          (recur
            (loop [dp dp j 1]
              (if (> j n)
                dp
                (recur
                  (if (= (nth str1 (dec i)) (nth str2 (dec j)))
                    (assoc-in dp [i j] (get-in dp [(dec i) (dec j)]))
                    (assoc-in dp [i j] (inc (min (get-in dp [(dec i) j])
                                                (get-in dp [i (dec j)])
                                                (get-in dp [(dec i) (dec j)])))))
                  (inc j))))
            (inc i)))))))

(println (edit-distance "kitten" "sitting"))
