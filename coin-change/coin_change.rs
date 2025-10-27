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
    println!("{}", coin_change(&[1, 3, 4], 6));
}