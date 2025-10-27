(defn gcd [a b]
  (if (zero? b) a (recur b (mod a b))))

(defn lcm [a b]
  (/ (* a b) (gcd a b)))

(defn extended-gcd [a b]
  (if (zero? b)
    [a 1 0]
    (let [[g x1 y1] (extended-gcd b (mod a b))
          x (- y1 (* (quot a b) x1))
          y x1]
      [g x y])))

(println "GCD:" (gcd 48 18))
(println "LCM:" (lcm 48 18))
(println "Extended GCD:" (extended-gcd 48 18))