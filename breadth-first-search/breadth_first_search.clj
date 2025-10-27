(defn bfs [graph start]
  (loop [queue [start] visited #{start}]
    (when (seq queue)
      (let [node (first queue)
            neighbors (get graph node [])
            new-neighbors (remove visited neighbors)
            new-visited (into visited new-neighbors)
            new-queue (into (vec (rest queue)) new-neighbors)]
        (print node " ")
        (recur new-queue new-visited)))))

(def graph {0 [1 2] 1 [2] 2 [0 3] 3 [3]})
(bfs graph 2)