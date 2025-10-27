(defn make-hash-table [size]
  {:size size :buckets (vec (repeat size []))})

(defn hash-fn [key size]
  (mod (hash key) size))

(defn put [ht key value]
  (let [index (hash-fn key (:size ht))
        bucket (nth (:buckets ht) index)
        new-bucket (conj (remove #(= (first %) key) bucket) [key value])]
    (assoc-in ht [:buckets index] new-bucket)))

(defn get-val [ht key]
  (let [index (hash-fn key (:size ht))
        bucket (nth (:buckets ht) index)
        pair (first (filter #(= (first %) key) bucket))]
    (when pair (second pair))))

(def ht (-> (make-hash-table 10)
            (put "key1" "value1")))
(println (get-val ht "key1"))