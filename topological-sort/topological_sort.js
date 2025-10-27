function topologicalSortDFS(graph, numVertices) {
    const visited = new Array(numVertices).fill(false);
    const stack = [];
    
    function dfs(v) {
        visited[v] = true;
        for (const neighbor of graph[v] || []) {
            if (!visited[neighbor]) {
                dfs(neighbor);
            }
        }
        stack.push(v);
    }
    
    for (let i = 0; i < numVertices; i++) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    
    return stack.reverse();
}

function topologicalSortKahn(graph, numVertices) {
    // Calculate in-degrees
    const inDegree = new Array(numVertices).fill(0);
    for (let u = 0; u < numVertices; u++) {
        for (const v of graph[u] || []) {
            inDegree[v]++;
        }
    }
    
    // Queue for vertices with 0 in-degree
    const queue = [];
    for (let i = 0; i < numVertices; i++) {
        if (inDegree[i] === 0) {
            queue.push(i);
        }
    }
    
    const result = [];
    
    while (queue.length > 0) {
        const u = queue.shift();
        result.push(u);
        
        for (const v of graph[u] || []) {
            inDegree[v]--;
            if (inDegree[v] === 0) {
                queue.push(v);
            }
        }
    }
    
    // Check for cycle
    if (result.length !== numVertices) {
        return null; // Cycle detected
    }
    
    return result;
}

function hasCycle(graph, numVertices) {
    const WHITE = 0, GRAY = 1, BLACK = 2;
    const color = new Array(numVertices).fill(WHITE);
    
    function dfs(v) {
        if (color[v] === GRAY) {
            return true; // Back edge found
        }
        if (color[v] === BLACK) {
            return false;
        }
        
        color[v] = GRAY;
        for (const neighbor of graph[v] || []) {
            if (dfs(neighbor)) {
                return true;
            }
        }
        color[v] = BLACK;
        return false;
    }
    
    for (let i = 0; i < numVertices; i++) {
        if (color[i] === WHITE) {
            if (dfs(i)) {
                return true;
            }
        }
    }
    return false;
}

// Test
const graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
};

const numVertices = 6;
console.log("DFS:", topologicalSortDFS(graph, numVertices)); // [5, 4, 2, 3, 1, 0]
console.log("Kahn:", topologicalSortKahn(graph, numVertices)); // [4, 5, 0, 2, 3, 1]
