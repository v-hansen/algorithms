#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int queue[MAX], front = 0, rear = 0;
int visited[MAX];
int adj[MAX][MAX];

void enqueue(int x) { queue[rear++] = x; }
int dequeue() { return queue[front++]; }
int isEmpty() { return front == rear; }

void bfs(int start, int n) {
    visited[start] = 1;
    enqueue(start);
    
    while (!isEmpty()) {
        int node = dequeue();
        printf("%d ", node);
        
        for (int i = 0; i < n; i++) {
            if (adj[node][i] && !visited[i]) {
                visited[i] = 1;
                enqueue(i);
            }
        }
    }
}

int main() {
    int n = 4;
    adj[0][1] = adj[0][2] = 1;
    adj[1][2] = 1;
    adj[2][0] = adj[2][3] = 1;
    adj[3][3] = 1;
    
    bfs(2, n);
    return 0;
}