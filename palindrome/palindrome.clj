(defn palindrome? [s]
  (let [cleaned (clojure.string/lower-case s)]
    (= cleaned (clojure.string/reverse cleaned))))

(println (palindrome? "racecar"))
(println (palindrome? "hello"))
