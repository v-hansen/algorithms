#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int visited[MAX];
int stack[MAX], top = -1;
int adj[MAX][MAX];

void push(int x) { stack[++top] = x; }
int pop() { return stack[top--]; }

void dfs(int v, int n) {
    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (adj[v][i] && !visited[i]) {
            dfs(i, n);
        }
    }
    push(v);
}

void topologicalSort(int n) {
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, n);
        }
    }
    
    while (top >= 0) {
        printf("%d ", pop());
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][3] = 1;
    adj[2][3] = 1;
    
    topologicalSort(n);
    return 0;
}