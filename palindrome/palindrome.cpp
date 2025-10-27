#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

bool isPalindrome(const string& s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) return false;
        left++;
        right--;
    }
    return true;
}

bool isPalindromeReverse(const string& s) {
    string reversed = s;
    reverse(reversed.begin(), reversed.end());
    return s == reversed;
}

bool isPalindromeClean(const string& s) {
    string cleaned;
    for (char c : s) {
        if (isalnum(c)) {
            cleaned += tolower(c);
        }
    }
    return isPalindrome(cleaned);
}

int main() {
    cout << isPalindrome("racecar") << endl;
    cout << isPalindromeReverse("level") << endl;
    cout << isPalindromeClean("A man, a plan, a canal: Panama") << endl;
    return 0;
}