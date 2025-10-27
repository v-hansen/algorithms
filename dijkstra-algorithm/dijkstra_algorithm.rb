def dijkstra(graph, start)
  distances = Hash.new(Float::INFINITY)
  distances[start] = 0
  pq = [[0, start]]
  
  while !pq.empty?
    pq.sort!
    current_distance, current = pq.shift
    next if current_distance > distances[current]
    
    graph[current].each do |neighbor, weight|
      distance = current_distance + weight
      if distance < distances[neighbor]
        distances[neighbor] = distance
        pq.push([distance, neighbor])
      end
    end
  end
  
  distances
end

graph = {'A' => {'B' => 1, 'C' => 4}, 'B' => {'C' => 2, 'D' => 5}, 'C' => {'D' => 1}, 'D' => {}}
puts dijkstra(graph, 'A').inspect