def fib_memo(n, memo = {})
  return memo[n] if memo.key?(n)
  return 1 if n <= 2
  memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
end

def coin_change(coins, amount)
  dp = Array.new(amount + 1, Float::INFINITY)
  dp[0] = 0
  
  coins.each do |coin|
    (coin..amount).each do |i|
      dp[i] = [dp[i], dp[i - coin] + 1].min
    end
  end
  dp[amount] == Float::INFINITY ? -1 : dp[amount]
end

puts "Fib(10): #{fib_memo(10)}"
puts "Coin change: #{coin_change([1, 3, 4], 6)}" 