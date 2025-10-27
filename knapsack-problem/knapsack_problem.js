function knapsack01(weights, values, capacity) {
    const n = weights.length;
    
    // Create DP table
    const dp = Array(n + 1).fill(null).map(() => Array(capacity + 1).fill(0));
    
    // Fill DP table
    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= capacity; w++) {
            if (weights[i-1] > w) {
                dp[i][w] = dp[i-1][w];
            } else {
                dp[i][w] = Math.max(
                    dp[i-1][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                );
            }
        }
    }
    
    return dp[n][capacity];
}

function knapsackWithItems(weights, values, capacity) {
    const n = weights.length;
    const dp = Array(n + 1).fill(null).map(() => Array(capacity + 1).fill(0));
    
    // Fill DP table
    for (let i = 1; i <= n; i++) {
        for (let w = 1; w <= capacity; w++) {
            if (weights[i-1] > w) {
                dp[i][w] = dp[i-1][w];
            } else {
                dp[i][w] = Math.max(
                    dp[i-1][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                );
            }
        }
    }
    
    // Backtrack to find selected items
    const selectedItems = [];
    let w = capacity;
    for (let i = n; i > 0; i--) {
        if (dp[i][w] !== dp[i-1][w]) {
            selectedItems.push(i-1);
            w -= weights[i-1];
        }
    }
    
    return {
        maxValue: dp[n][capacity],
        items: selectedItems.reverse()
    };
}

function knapsackOptimized(weights, values, capacity) {
    const n = weights.length;
    const dp = new Array(capacity + 1).fill(0);
    
    for (let i = 0; i < n; i++) {
        for (let w = capacity; w >= weights[i]; w--) {
            dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }
    
    return dp[capacity];
}

// Test
const weights = [1, 3, 4, 5];
const values = [1, 4, 5, 7];
const capacity = 7;

const maxValue = knapsack01(weights, values, capacity);
console.log(`Maximum value: ${maxValue}`); // 9

const result = knapsackWithItems(weights, values, capacity);
console.log(`Maximum value: ${result.maxValue}, Items: ${result.items}`); // 9, [1, 2]
