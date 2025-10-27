#include <iostream>
#include <vector>
#include <stack>
#include <unordered_set>
using namespace std;

void dfs(int node, const vector<vector<int>>& graph, unordered_set<int>& visited, stack<int>& topoStack) {
    visited.insert(node);
    
    for (int neighbor : graph[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, graph, visited, topoStack);
        }
    }
    
    topoStack.push(node);
}

vector<int> topologicalSort(const vector<vector<int>>& graph) {
    unordered_set<int> visited;
    stack<int> topoStack;
    
    for (int i = 0; i < graph.size(); i++) {
        if (visited.find(i) == visited.end()) {
            dfs(i, graph, visited, topoStack);
        }
    }
    
    vector<int> result;
    while (!topoStack.empty()) {
        result.push_back(topoStack.top());
        topoStack.pop();
    }
    
    return result;
}

int main() {
    vector<vector<int>> graph = {{1, 2}, {3}, {3}, {}};
    auto result = topologicalSort(graph);
    
    for (int node : result) {
        cout << node << " ";
    }
    cout << endl;
    
    return 0;
}