#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

void bfs(int start, const vector<vector<int>>& graph) {
    unordered_set<int> visited;
    queue<int> q;
    
    visited.insert(start);
    q.push(start);
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";
        
        for (int neighbor : graph[node]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push(neighbor);
            }
        }
    }
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {2}, {0, 3}, {3}};
    bfs(2, graph);
    return 0;
}