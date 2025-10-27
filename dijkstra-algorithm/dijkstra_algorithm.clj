(defn dijkstra [graph start]
  (loop [distances (assoc (zipmap (keys graph) (repeat Double/POSITIVE_INFINITY)) start 0)
         pq [[0 start]]]
    (if (empty? pq)
      distances
      (let [[current-distance current] (first (sort pq))
            remaining-pq (remove #(= % [current-distance current]) pq)]
        (if (> current-distance (get distances current))
          (recur distances remaining-pq)
          (let [neighbors (get graph current {})
                updates (for [[neighbor weight] neighbors
                             :let [distance (+ current-distance weight)]
                             :when (< distance (get distances neighbor))]
                         [neighbor distance])
                new-distances (reduce (fn [d [n dist]] (assoc d n dist)) distances updates)
                new-pq (concat remaining-pq (map (fn [[n d]] [d n]) updates))]
            (recur new-distances new-pq)))))))

(def graph {"A" {"B" 1 "C" 4} "B" {"C" 2 "D" 5} "C" {"D" 1} "D" {}})
(println (dijkstra graph "A"))