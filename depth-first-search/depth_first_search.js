function dfs(graph, start, visited = new Set()) {
    visited.add(start);
    process.stdout.write(start + ' ');
    (graph[start] || []).forEach(neighbor => {
        if (!visited.has(neighbor)) dfs(graph, neighbor, visited);
    });
    return visited;
}

const graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]};
dfs(graph, 2);