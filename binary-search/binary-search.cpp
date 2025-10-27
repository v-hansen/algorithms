#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    std::vector<int> arr = {1, 3, 5, 7, 9, 11};
    std::cout << binarySearch(arr, 7) << std::endl;
    std::cout << binarySearch(arr, 4) << std::endl;
    return 0;
}
