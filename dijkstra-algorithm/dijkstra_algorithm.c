#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define V 4

int minDistance(int dist[], bool sptSet[]) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++)
        if (!sptSet[v] && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

void dijkstra(int graph[V][V], int src) {
    int dist[V];
    bool sptSet[V];
    
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;
    
    dist[src] = 0;
    
    for (int count = 0; count < V - 1; count++) {
        int u = minDistance(dist, sptSet);
        sptSet[u] = true;
        
        for (int v = 0; v < V; v++)
            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
                dist[v] = dist[u] + graph[u][v];
    }
    
    for (int i = 0; i < V; i++)
        printf("%d: %d\n", i, dist[i]);
}

int main() {
    int graph[V][V] = {{0, 1, 4, 0}, {1, 0, 2, 5}, {4, 2, 0, 1}, {0, 5, 1, 0}};
    dijkstra(graph, 0);
    return 0;
}