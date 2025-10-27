#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isPalindrome(char str[]) {
    int left = 0, right = strlen(str) - 1;
    while (left < right) {
        if (tolower(str[left++]) != tolower(str[right--])) return 0;
    }
    return 1;
}

int main() {
    printf("%s\n", isPalindrome("racecar") ? "true" : "false");
    printf("%s\n", isPalindrome("hello") ? "true" : "false");
    return 0;
}
