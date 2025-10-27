#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    std::vector<int> arr = {5, 2, 8, 1, 9, 3};
    std::cout << linearSearch(arr, 8) << std::endl;
    std::cout << linearSearch(arr, 7) << std::endl;
    return 0;
}
