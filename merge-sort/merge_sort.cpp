#include <iostream>
#include <vector>
using namespace std;

vector<int> merge(const vector<int>& left, const vector<int>& right) {
    vector<int> result;
    size_t i = 0, j = 0;
    
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            result.push_back(left[i++]);
        } else {
            result.push_back(right[j++]);
        }
    }
    
    while (i < left.size()) result.push_back(left[i++]);
    while (j < right.size()) result.push_back(right[j++]);
    
    return result;
}

vector<int> mergeSort(const vector<int>& arr) {
    if (arr.size() <= 1) return arr;
    
    size_t mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    
    return merge(mergeSort(left), mergeSort(right));
}

int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    auto sorted = mergeSort(arr);
    for (int x : sorted) cout << x << " ";
    cout << endl;
}
