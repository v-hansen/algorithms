(defn euclidean-distance [p1 p2]
  (Math/sqrt (reduce + (map #(* (- %1 %2) (- %1 %2)) p1 p2))))

(defn closest-centroid [point centroids]
  (first (apply min-key second 
                (map-indexed #(vector %1 (euclidean-distance point %2)) centroids))))

(defn update-centroids [points labels k]
  (for [i (range k)]
    (let [cluster-points (map first (filter #(= i (second %)) (map vector points labels)))]
      (if (empty? cluster-points)
        (repeat (count (first points)) 0)
        (map #(/ (reduce +' %) (count cluster-points))
             (apply map vector cluster-points))))))

(defn k-means [points k max-iters]
  (let [n-points (count points)
        initial-centroids (take k (shuffle points))]
    (loop [centroids initial-centroids
           iter 0]
      (if (>= iter max-iters)
        (map #(closest-centroid % centroids) points)
        (let [labels (map #(closest-centroid % centroids) points)
              new-centroids (update-centroids points labels k)]
          (recur new-centroids (inc iter)))))))

(let [X [[1 2] [1 4] [1 0] [10 2] [10 4] [10 0]]
      labels (k-means X 2 100)]
  (println labels))
