#include <stdio.h>
int two_sum(int arr[], int n, int target, int result[]) {
    int left = 0, right = n - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) {
            result[0] = left;
            result[1] = right;
            return 1;
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return 0;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int result[2];
    if (two_sum(arr, 5, 7, result)) {
        printf("[%d, %d]\n", result[0], result[1]);
    }
    return 0;
}