#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int editDistance(const string& str1, const string& str2) {
    int m = str1.length();
    int n = str2.length();
    
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }
    }
    
    return dp[m][n];
}

int main() {
    string str1 = "kitten";
    string str2 = "sitting";
    int distance = editDistance(str1, str2);
    cout << "Edit distance between '" << str1 << "' and '" << str2 << "': " << distance << endl;
    return 0;
}
