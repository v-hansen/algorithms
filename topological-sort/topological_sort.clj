(defn topological-sort [graph]
  (let [visited (atom #{})
        stack (atom [])]
    (letfn [(dfs [node]
              (when-not (@visited node)
                (swap! visited conj node)
                (doseq [neighbor (get graph node [])]
                  (dfs neighbor))
                (swap! stack conj node)))]
      (doseq [node (keys graph)] (dfs node))
      (reverse @stack))))

(println (topological-sort {0 [1 2] 1 [3] 2 [3] 3 []}))