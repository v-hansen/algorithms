#include <iostream>
#include <vector>
using namespace std;

int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n-1) + fibRecursive(n-2);
}

int fibIterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int fibMemoized(int n, vector<int>& memo) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibMemoized(n-1, memo) + fibMemoized(n-2, memo);
    return memo[n];
}

int main() {
    cout << "Recursive: " << fibRecursive(10) << endl;
    cout << "Iterative: " << fibIterative(10) << endl;
    
    vector<int> memo(11, -1);
    cout << "Memoized: " << fibMemoized(10, memo) << endl;
    return 0;
}