fn lcs(x: &str, y: &str) -> usize {
    let x_chars: Vec<char> = x.chars().collect();
    let y_chars: Vec<char> = y.chars().collect();
    let m = x_chars.len();
    let n = y_chars.len();
    
    let mut dp = vec![vec![0; n + 1]; m + 1];
    
    for i in 1..=m {
        for j in 1..=n {
            if x_chars[i-1] == y_chars[j-1] {
                dp[i][j] = dp[i-1][j-1] + 1;
            } else {
                dp[i][j] = dp[i-1][j].max(dp[i][j-1]);
            }
        }
    }
    
    dp[m][n]
}

fn main() {
    println!("{}", lcs("ABCDGH", "AEDFHR"));
}