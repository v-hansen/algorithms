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

puts coin_change([1, 3, 4], 6)