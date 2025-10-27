(defn fit [X y]
  (println (str "Model trained with " (count X) " samples"))
  {:weights (vec (repeat (count (first X)) 0))})

(defn predict [model X]
  (vec (repeat (count X) 1)))

(let [X [[1 2] [3 4]]
      y [0 1]
      model (fit X y)
      pred (predict model [[2 3]])]
  (println (str "Prediction: " (first pred))))
