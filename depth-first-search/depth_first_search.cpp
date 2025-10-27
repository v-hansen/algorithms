#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

void dfs(int node, const vector<vector<int>>& graph, unordered_set<int>& visited) {
    visited.insert(node);
    cout << node << " ";
    
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited);
        }
    }
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {2}, {0, 3}, {3}};
    unordered_set<int> visited;
    dfs(2, graph, visited);
    return 0;
}