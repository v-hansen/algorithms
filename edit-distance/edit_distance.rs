fn edit_distance(s1: &str, s2: &str) -> usize {
    let s1: Vec<char> = s1.chars().collect();
    let s2: Vec<char> = s2.chars().collect();
    let m = s1.len();
    let n = s2.len();
    
    let mut dp = vec![vec![0; n + 1]; m + 1];
    
    for i in 0..=m { dp[i][0] = i; }
    for j in 0..=n { dp[0][j] = j; }
    
    for i in 1..=m {
        for j in 1..=n {
            if s1[i-1] == s2[j-1] {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + dp[i-1][j].min(dp[i][j-1]).min(dp[i-1][j-1]);
            }
        }
    }
    
    dp[m][n]
}

fn main() {
    println!("{}", edit_distance("kitten", "sitting"));
}