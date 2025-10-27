#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<int> computeLPS(const string& pattern) {
    int m = pattern.length();
    vector<int> lps(m, 0);
    int length = 0;
    int i = 1;
    
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
    return lps;
}

vector<int> kmpSearch(const string& text, const string& pattern) {
    int n = text.length();
    int m = pattern.length();
    
    if (m == 0) return {};
    
    vector<int> lps = computeLPS(pattern);
    vector<int> matches;
    
    int i = 0, j = 0;
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }
        
        if (j == m) {
            matches.push_back(i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    
    return matches;
}

int main() {
    string text = "ABABDABACDABABCABCABCABCABC";
    string pattern = "ABABCABCABCABC";
    vector<int> matches = kmpSearch(text, pattern);
    
    cout << "Pattern found at indices: ";
    for (int match : matches) {
        cout << match << " ";
    }
    cout << endl;
    return 0;
}
