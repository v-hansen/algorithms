from collections import defaultdict, deque

def topological_sort_dfs(graph, num_vertices):
    """Topological sort using DFS"""
    visited = [False] * num_vertices
    stack = []
    
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)
    
    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

def topological_sort_kahn(graph, num_vertices):
    """Topological sort using Kahn's algorithm (BFS)"""
    # Calculate in-degrees
    in_degree = [0] * num_vertices
    for u in range(num_vertices):
        for v in graph[u]:
            in_degree[v] += 1
    
    # Queue for vertices with 0 in-degree
    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check for cycle
    if len(result) != num_vertices:
        return None  # Cycle detected
    
    return result

def has_cycle(graph, num_vertices):
    """Check if graph has cycle using DFS"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_vertices
    
    def dfs(v):
        if color[v] == GRAY:
            return True  # Back edge found
        if color[v] == BLACK:
            return False
        
        color[v] = GRAY
        for neighbor in graph[v]:
            if dfs(neighbor):
                return True
        color[v] = BLACK
        return False
    
    for i in range(num_vertices):
        if color[i] == WHITE:
            if dfs(i):
                return True
    return False

# Test
graph = defaultdict(list)
graph[5] = [2, 0]
graph[4] = [0, 1]
graph[2] = [3]
graph[3] = [1]

num_vertices = 6
print("DFS:", topological_sort_dfs(graph, num_vertices))  # [5, 4, 2, 3, 1, 0]
print("Kahn:", topological_sort_kahn(graph, num_vertices))  # [4, 5, 0, 2, 3, 1]
