#include <stdio.h>

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int main() {
    int arr[] = {5, 2, 8, 1, 9, 3};
    int size = sizeof(arr) / sizeof(arr[0]);
    printf("%d\n", linearSearch(arr, size, 8));
    printf("%d\n", linearSearch(arr, size, 7));
    return 0;
}
