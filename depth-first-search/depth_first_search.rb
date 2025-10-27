def dfs(graph, start, visited = Set.new)
  return if visited.include?(start)
  
  visited.add(start)
  print "#{start} "
  
  (graph[start] || []).each do |neighbor|
    dfs(graph, neighbor, visited)
  end
end

graph = {0 => [1, 2], 1 => [2], 2 => [0, 3], 3 => [3]}
dfs(graph, 2)