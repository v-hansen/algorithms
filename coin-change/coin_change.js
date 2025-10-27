function coinChange(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
}

function coinChangeWays(coins, amount) {
    const dp = new Array(amount + 1).fill(0);
    dp[0] = 1;
    
    for (const coin of coins) {
        for (let i = coin; i <= amount; i++) {
            dp[i] += dp[i - coin];
        }
    }
    
    return dp[amount];
}

function coinChangeWithCoins(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    const parent = new Array(amount + 1).fill(-1);
    dp[0] = 0;
    
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (coin <= i && dp[i - coin] + 1 < dp[i]) {
                dp[i] = dp[i - coin] + 1;
                parent[i] = coin;
            }
        }
    }
    
    if (dp[amount] === Infinity) {
        return { minCoins: -1, coins: [] };
    }
    
    // Reconstruct solution
    const resultCoins = [];
    let curr = amount;
    while (curr > 0) {
        const coin = parent[curr];
        resultCoins.push(coin);
        curr -= coin;
    }
    
    return { minCoins: dp[amount], coins: resultCoins };
}

// Test
const coins = [1, 3, 4];
const amount = 6;
console.log(`Min coins for ${amount}: ${coinChange(coins, amount)}`); // 2
console.log(`Ways to make ${amount}: ${coinChangeWays(coins, amount)}`); // 2
