#include <stdio.h>
int linearSearch(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int linearSearchRecursive(int arr[], int n, int target, int index) {
    if (index >= n) return -1;
    if (arr[index] == target) return index;
    return linearSearchRecursive(arr, n, target, index + 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("Iterative: %d\n", linearSearch(arr, n, 3));
    printf("Recursive: %d\n", linearSearchRecursive(arr, n, 3, 0));
    return 0;
}