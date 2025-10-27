def fibonacci(n)
  return n if n <= 1
  
  a, b = 0, 1
  (2..n).each do
    a, b = b, a + b
  end
  b
end

def fibonacci_sequence(count)
  (0...count).map { |i| fibonacci(i) }
end

# Versão com Enumerator (lazy)
def fibonacci_lazy
  Enumerator.new do |yielder|
    a, b = 0, 1
    loop do
      yielder << a
      a, b = b, a + b
    end
  end
end

# Exemplo de uso
puts "Sequência de Fibonacci:"
fibonacci_sequence(15).each_with_index do |value, index|
  puts "F(#{index}) = #{value}"
end

puts "\nF(20) = #{fibonacci(20)}"

puts "\nPrimeiros 10 números (lazy):"
puts fibonacci_lazy.take(10).to_a.inspect