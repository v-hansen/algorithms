fn knapsack(weights: &[i32], values: &[i32], capacity: i32) -> i32 {
    let n = weights.len();
    let mut dp = vec![vec![0; (capacity + 1) as usize]; n + 1];
    
    for i in 1..=n {
        for w in 1..=capacity {
            if weights[i-1] <= w {
                dp[i][w as usize] = dp[i-1][w as usize].max(
                    dp[i-1][(w - weights[i-1]) as usize] + values[i-1]
                );
            } else {
                dp[i][w as usize] = dp[i-1][w as usize];
            }
        }
    }
    
    dp[n][capacity as usize]
}

fn main() {
    println!("{}", knapsack(&[2, 1, 3], &[4, 2, 3], 4));
}