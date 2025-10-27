function topologicalSort(graph: {[key: number]: number[]}): number[] {
    const visited = new Set<number>();
    const stack: number[] = [];
    
    function dfs(node: number): void {
        if (visited.has(node)) return;
        visited.add(node);
        
        for (const neighbor of graph[node] || []) {
            dfs(neighbor);
        }
        
        stack.push(node);
    }
    
    for (const node in graph) {
        dfs(parseInt(node));
    }
    
    return stack.reverse();
}

const graph = {0: [1, 2], 1: [3], 2: [3], 3: []};
console.log(topologicalSort(graph));