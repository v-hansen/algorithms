def is_palindrome_simple(s):
    return s == s[::-1]

def is_palindrome_two_pointers(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_clean(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome_simple("racecar"))
print(is_palindrome_two_pointers("A man a plan a canal Panama"))
print(is_palindrome_clean("race a car"))