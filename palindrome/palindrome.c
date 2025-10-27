#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (s[left] != s[right]) return 0;
        left++;
        right--;
    }
    return 1;
}

int isPalindromeIgnoreCase(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        if (tolower(s[left]) != tolower(s[right])) return 0;
        left++;
        right--;
    }
    return 1;
}

int isPalindromeAlphanumeric(char* s) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        if (tolower(s[left]) != tolower(s[right])) return 0;
        left++;
        right--;
    }
    return 1;
}

int main() {
    printf("%d\n", isPalindrome("racecar"));
    printf("%d\n", isPalindromeIgnoreCase("RaceCar"));
    printf("%d\n", isPalindromeAlphanumeric("A man, a plan, a canal: Panama"));
    return 0;
}