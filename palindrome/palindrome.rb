def palindrome?(str)
  str.downcase == str.downcase.reverse
end

puts palindrome?("racecar")
puts palindrome?("hello")
