from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

# Test
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
