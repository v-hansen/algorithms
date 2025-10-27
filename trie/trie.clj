(defn make-trie-node [] {:children {} :is-end false})

(defn insert-word [trie word]
  (reduce (fn [node char]
           (update-in node [:children char] #(or % (make-trie-node))))
         trie word)
  (assoc-in trie (concat [:children] (interleave word (repeat :children)) [:is-end]) true))

(defn search-word [trie word]
  (let [path (concat [:children] (interleave word (repeat :children)) [:is-end])]
    (get-in trie path false)))

(def trie (-> (make-trie-node)
              (insert-word "hello")))
(println (search-word trie "hello"))