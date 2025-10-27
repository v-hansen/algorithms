#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {left, right};
        else if (sum < target) left++;
        else right--;
    }
    return {};
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    auto result = twoSum(arr, 7);
    if (!result.empty()) {
        cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    }
    return 0;
}