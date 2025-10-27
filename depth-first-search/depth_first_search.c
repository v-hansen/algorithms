#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int visited[MAX];
int adj[MAX][MAX];

void dfs(int v, int n) {
    visited[v] = 1;
    printf("%d ", v);
    
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i, n);
        }
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][2] = 1;
    adj[2][0] = adj[2][3] = 1;
    adj[3][3] = 1;
    
    dfs(2, n);
    return 0;
}