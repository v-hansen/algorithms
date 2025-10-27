(defn make-node [data next] {:data data :next next})

(defn append [head data]
  (if (nil? head)
    (make-node data nil)
    (assoc head :next (append (:next head) data))))

(defn display [head]
  (when head
    (print (:data head) " -> ")
    (display (:next head))))

(def ll (reduce append nil [1 2 3]))
(display ll)
(println "nil")