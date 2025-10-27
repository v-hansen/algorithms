def knapsack_01(weights, values, capacity):
    """0/1 Knapsack Problem using Dynamic Programming"""
    n = len(weights)
    
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If current item weight is more than capacity, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude current item
                    values[i-1] + dp[i-1][w - weights[i-1]]  # include current item
                )
    
    return dp[n][capacity]

def knapsack_with_items(weights, values, capacity):
    """Return maximum value and selected items"""
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(
                    dp[i-1][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                )
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    return dp[n][capacity], selected_items[::-1]

def knapsack_optimized(weights, values, capacity):
    """Space-optimized version using 1D array"""
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    
    return dp[capacity]

# Test
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value = knapsack_01(weights, values, capacity)
print(f"Maximum value: {max_value}")  # 9

max_value, items = knapsack_with_items(weights, values, capacity)
print(f"Maximum value: {max_value}, Items: {items}")  # 9, [1, 2]
