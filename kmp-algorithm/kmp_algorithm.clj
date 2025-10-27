(defn compute-lps [pattern]
  (loop [lps (vec (repeat (count pattern) 0))
         len 0
         i 1]
    (cond
      (>= i (count pattern)) lps
      (= (nth pattern i) (nth pattern len))
      (recur (assoc lps i (inc len)) (inc len) (inc i))
      (not= len 0)
      (recur lps (nth lps (dec len)) i)
      :else
      (recur (assoc lps i 0) len (inc i)))))

(defn kmp-search [text pattern]
  (let [lps (compute-lps pattern)]
    (loop [i 0 j 0 matches []]
      (cond
        (>= i (count text)) matches
        (= (nth pattern j) (nth text i))
        (let [new-i (inc i) new-j (inc j)]
          (if (= new-j (count pattern))
            (recur new-i (nth lps (dec new-j)) (conj matches (- new-i new-j)))
            (recur new-i new-j matches)))
        (and (< i (count text)) (not= (nth pattern j) (nth text i)))
        (if (not= j 0)
          (recur i (nth lps (dec j)) matches)
          (recur (inc i) j matches))
        :else matches))))

(println (kmp-search "ABABDABACDABABCABCABCABCABC" "ABABCABCABCABC"))