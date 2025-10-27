def bfs(graph, start)
  visited = Set.new
  queue = [start]
  visited.add(start)
  
  while !queue.empty?
    node = queue.shift
    print "#{node} "
    
    (graph[node] || []).each do |neighbor|
      unless visited.include?(neighbor)
        visited.add(neighbor)
        queue.push(neighbor)
      end
    end
  end
end

graph = {0 => [1, 2], 1 => [2], 2 => [0, 3], 3 => [3]}
bfs(graph, 2)