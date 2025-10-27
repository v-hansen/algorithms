#include <iostream>
#include <string>
#include <algorithm>

bool isPalindrome(std::string str) {
    std::transform(str.begin(), str.end(), str.begin(), ::tolower);
    std::string reversed = str;
    std::reverse(reversed.begin(), reversed.end());
    return str == reversed;
}

int main() {
    std::cout << std::boolalpha << isPalindrome("racecar") << std::endl;
    std::cout << std::boolalpha << isPalindrome("hello") << std::endl;
    return 0;
}
