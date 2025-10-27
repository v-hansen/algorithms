function bfs(graph, start) {
    const visited = new Set();
    const queue = [start];
    visited.add(start);
    
    while (queue.length > 0) {
        const node = queue.shift();
        process.stdout.write(node + " ");
        
        const neighbors = graph[node] || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
}

const graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]};
bfs(graph, 2);