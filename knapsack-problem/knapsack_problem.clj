(defn knapsack [weights values capacity]
  (let [n (count weights)
        dp (vec (for [i (range (inc n))]
                 (vec (repeat (inc capacity) 0))))]
    (reduce (fn [dp i]
             (reduce (fn [dp w]
                      (let [weight (nth weights (dec i))
                            value (nth values (dec i))]
                        (if (<= weight w)
                          (assoc-in dp [i w] 
                                   (max (get-in dp [(dec i) w])
                                        (+ (get-in dp [(dec i) (- w weight)]) value)))
                          (assoc-in dp [i w] (get-in dp [(dec i) w])))))
                    dp (range 1 (inc capacity))))
           dp (range 1 (inc n)))
    (get-in dp [n capacity])))

(println (knapsack [2 1 3] [4 2 3] 4))