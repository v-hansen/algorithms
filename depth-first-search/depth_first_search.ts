function dfs(graph: {[key: number]: number[]}, start: number, visited: Set<number>): void {
    visited.add(start);
    process.stdout.write(start + " ");
    
    const neighbors = graph[start] || [];
    for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
            dfs(graph, neighbor, visited);
        }
    }
}

const graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
};

const visited = new Set<number>();
dfs(graph, 2, visited);