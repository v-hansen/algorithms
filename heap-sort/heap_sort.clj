(defn heapify [arr n i]
  (let [largest i
        left (+ (* 2 i) 1)
        right (+ (* 2 i) 2)
        largest (if (and (< left n) (> (nth arr left) (nth arr largest))) left largest)
        largest (if (and (< right n) (> (nth arr right) (nth arr largest))) right largest)]
    (if (not= largest i)
      (let [new-arr (assoc arr i (nth arr largest) largest (nth arr i))]
        (heapify new-arr n largest))
      arr)))

(defn heap-sort [arr]
  (let [n (count arr)
        arr (reduce #(heapify %1 n %2) arr (range (dec (quot n 2)) -1 -1))]
    (reduce (fn [acc i]
              (let [new-arr (assoc acc 0 (nth acc i) i (nth acc 0))]
                (heapify new-arr i 0)))
            arr (range (dec n) 0 -1))))

(println (heap-sort [64 34 25 12 22 11 90]))