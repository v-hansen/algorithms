def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_ways(coins, amount):
    """Number of ways to make amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

def coin_change_with_coins(coins, amount):
    """Return minimum coins and the actual coins used"""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct solution
    result_coins = []
    curr = amount
    while curr > 0:
        coin = parent[curr]
        result_coins.append(coin)
        curr -= coin
    
    return dp[amount], result_coins

# Test
coins = [1, 3, 4]
amount = 6
print(f"Min coins for {amount}: {coin_change(coins, amount)}")  # 2
print(f"Ways to make {amount}: {coin_change_ways(coins, amount)}")  # 2
