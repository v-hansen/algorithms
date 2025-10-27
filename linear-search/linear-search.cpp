#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int linearSearch(const vector<int>& arr, int target) {
    auto it = find(arr.begin(), arr.end(), target);
    return it != arr.end() ? distance(arr.begin(), it) : -1;
}

int linearSearchManual(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << "STL: " << linearSearch(arr, 3) << endl;
    cout << "Manual: " << linearSearchManual(arr, 3) << endl;
    return 0;
}