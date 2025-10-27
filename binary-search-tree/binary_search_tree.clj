(defn make-node [data] {:data data :left nil :right nil})

(defn insert-node [node data]
  (cond
    (nil? node) (make-node data)
    (< data (:data node)) (assoc node :left (insert-node (:left node) data))
    :else (assoc node :right (insert-node (:right node) data))))

(defn search-node [node data]
  (cond
    (or (nil? node) (= (:data node) data)) node
    (< data (:data node)) (search-node (:left node) data)
    :else (search-node (:right node) data)))

(def bst (reduce insert-node nil [50 30 70 20 40]))
(println (if (search-node bst 40) "Found" "Not found"))