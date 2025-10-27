#include <stdio.h>

int* twoSum(int* arr, int size, int target, int* result) {
    int left = 0, right = size - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            result[0] = left; result[1] = right;
            return result;
        }
        sum < target ? left++ : right--;
    }
    return NULL;
}

int main() {
    int arr[] = {1, 2, 3, 4, 6};
    int result[2];
    twoSum(arr, 5, 6, result);
    printf("[%d, %d]\n", result[0], result[1]);
}
