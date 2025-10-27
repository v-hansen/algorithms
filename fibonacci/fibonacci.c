#include <stdio.h>
int fibRecursive(int n) {
    if (n <= 1) return n;
    return fibRecursive(n-1) + fibRecursive(n-2);
}

int fibIterative(int n) {
    if (n <= 1) return n;
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

int main() {
    printf("Recursive: %d\n", fibRecursive(10));
    printf("Iterative: %d\n", fibIterative(10));
    return 0;
}