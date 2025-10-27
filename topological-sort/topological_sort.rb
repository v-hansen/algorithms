def topological_sort(graph)
  visited = Set.new
  stack = []
  
  def dfs(node)
    return if visited.include?(node)
    visited.add(node)
    (graph[node] || []).each { |neighbor| dfs(neighbor) }
    stack.push(node)
  end
  
  graph.keys.each { |node| dfs(node) }
  stack.reverse
end

puts topological_sort({0 => [1, 2], 1 => [3], 2 => [3], 3 => []}).inspect