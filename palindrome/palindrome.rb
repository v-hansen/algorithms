def palindrome_simple?(s)
  s == s.reverse
end

def palindrome_two_pointers?(s)
  left, right = 0, s.length - 1
  while left < right
    return false if s[left] != s[right]
    left += 1
    right -= 1
  end
  true
end

def palindrome_clean?(s)
  cleaned = s.downcase.gsub(/[^a-z0-9]/, '')
  cleaned == cleaned.reverse
end

puts palindrome_simple?("racecar")
puts palindrome_two_pointers?("A man a plan a canal Panama")
puts palindrome_clean?("race a car")