function dijkstra(graph, start) {
    const distances = {};
    const pq = [[0, start]];
    
    for (let node in graph) distances[node] = Infinity;
    distances[start] = 0;
    
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const [currentDistance, current] = pq.shift();
        
        if (currentDistance > distances[current]) continue;
        
        for (let neighbor in graph[current]) {
            const distance = currentDistance + graph[current][neighbor];
            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                pq.push([distance, neighbor]);
            }
        }
    }
    return distances;
}

const graph = {A: {B: 1, C: 4}, B: {C: 2, D: 5}, C: {D: 1}, D: {}};
console.log(dijkstra(graph, 'A'));