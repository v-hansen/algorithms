fn fibonacci(n: usize) -> u64 {
    if n <= 1 { return n as u64; }
    let mut dp = vec![0u64; n + 1];
    dp[1] = 1;
    for i in 2..=n {
        dp[i] = dp[i-1] + dp[i-2];
    }
    dp[n]
}

fn coin_change(coins: &[i32], amount: i32) -> i32 {
    let mut dp = vec![i32::MAX; (amount + 1) as usize];
    dp[0] = 0;
    
    for &coin in coins {
        for i in coin..=amount {
            if dp[(i - coin) as usize] != i32::MAX {
                dp[i as usize] = dp[i as usize].min(dp[(i - coin) as usize] + 1);
            }
        }
    }
    
    if dp[amount as usize] == i32::MAX { -1 } else { dp[amount as usize] }
}

fn main() {
    println!("Fibonacci(10): {}", fibonacci(10));
    println!("Coin change: {}", coin_change(&[1, 3, 4], 6));
}