#include <vector>
#include <iostream>
using namespace std;

vector<int> twoSum(vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {left, right};
        sum < target ? left++ : right--;
    }
    return {};
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 6};
    auto result = twoSum(arr, 6);
    cout << "[" << result[0] << ", " << result[1] << "]" << endl;
}
