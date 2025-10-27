function dijkstra(graph: number[][], src: number): number[] {
    const V = graph.length;
    const dist = new Array(V).fill(Infinity);
    const sptSet = new Array(V).fill(false);
    
    dist[src] = 0;
    
    for (let count = 0; count < V - 1; count++) {
        const u = minDistance(dist, sptSet);
        sptSet[u] = true;
        
        for (let v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] !== Infinity && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }
    
    return dist;
}

function minDistance(dist: number[], sptSet: boolean[]): number {
    let min = Infinity;
    let minIndex = 0;
    
    for (let v = 0; v < dist.length; v++) {
        if (!sptSet[v] && dist[v] <= min) {
            min = dist[v];
            minIndex = v;
        }
    }
    
    return minIndex;
}

const graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
];

const result = dijkstra(graph, 0);
result.forEach((d, i) => console.log(`${i}: ${d}`));