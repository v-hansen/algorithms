def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

def lcm(a, b)
  (a * b) / gcd(a, b)
end

def extended_gcd(a, b)
  return [a, 1, 0] if b == 0
  
  g, x1, y1 = extended_gcd(b, a % b)
  x = y1
  y = x1 - (a / b) * y1
  
  [g, x, y]
end

puts "GCD: #{gcd(48, 18)}"
puts "LCM: #{lcm(48, 18)}"
puts "Extended GCD: #{extended_gcd(48, 18)}" 