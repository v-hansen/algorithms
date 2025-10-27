#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void computeLPS(char* pattern, int* lps) {
    int m = strlen(pattern);
    int length = 0;
    int i = 1;
    lps[0] = 0;
    
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
}

void kmpSearch(char* text, char* pattern) {
    int n = strlen(text);
    int m = strlen(pattern);
    
    int* lps = (int*)malloc(m * sizeof(int));
    computeLPS(pattern, lps);
    
    int i = 0, j = 0;
    printf("Pattern found at indices: ");
    
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }
        
        if (j == m) {
            printf("%d ", i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    printf("\n");
    free(lps);
}

int main() {
    char text[] = "ABABDABACDABABCABCABCABCABC";
    char pattern[] = "ABABCABCABCABC";
    kmpSearch(text, pattern);
    return 0;
}
