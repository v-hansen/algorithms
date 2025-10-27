(defn dfs [graph start visited]
  (let [new-visited (conj visited start)]
    (print start " ")
    (reduce (fn [v neighbor]
              (if (contains? v neighbor)
                v
                (dfs graph neighbor v)))
            new-visited
            (get graph start []))))

(def graph {0 [1 2] 1 [2] 2 [0 3] 3 [3]})
(dfs graph 2 #{})