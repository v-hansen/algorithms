#!/usr/bin/env python3
import os

def complete_palindrome():
    """Completa todas as implementações de palindrome"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/palindrome"
    
    files_to_expand = [
        ("palindrome.py", """def is_palindrome_simple(s):
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
print(is_palindrome_clean("race a car"))"""),
        
        ("palindrome.js", """function isPalindromeSimple(s) {
    return s === s.split('').reverse().join('');
}

function isPalindromeTwoPointers(s) {
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}

function isPalindromeClean(s) {
    const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
}

console.log(isPalindromeSimple("racecar"));
console.log(isPalindromeTwoPointers("A man a plan a canal Panama"));
console.log(isPalindromeClean("race a car"));"""),
        
        ("palindrome.rb", """def palindrome_simple?(s)
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
puts palindrome_clean?("race a car")"""),
        
        ("palindrome.ts", """function isPalindromeSimple(s: string): boolean {
    return s === s.split('').reverse().join('');
}

function isPalindromeTwoPointers(s: string): boolean {
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
}

function isPalindromeClean(s: string): boolean {
    const cleaned = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleaned === cleaned.split('').reverse().join('');
}

console.log(isPalindromeSimple("racecar"));
console.log(isPalindromeTwoPointers("A man a plan a canal Panama"));
console.log(isPalindromeClean("race a car"));""")
    ]
    
    for filename, code in files_to_expand:
        with open(f"{base_dir}/{filename}", "w") as f:
            f.write(code)

def complete_kmp_algorithm():
    """Completa implementações do KMP que são placeholders"""
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/kmp-algorithm"
    
    # Ruby
    with open(f"{base_dir}/kmp_algorithm.rb", "w") as f:
        f.write("""def compute_lps(pattern)
  lps = Array.new(pattern.length, 0)
  len = 0
  i = 1
  
  while i < pattern.length
    if pattern[i] == pattern[len]
      len += 1
      lps[i] = len
      i += 1
    else
      if len != 0
        len = lps[len - 1]
      else
        lps[i] = 0
        i += 1
      end
    end
  end
  lps
end

def kmp_search(text, pattern)
  lps = compute_lps(pattern)
  i = j = 0
  matches = []
  
  while i < text.length
    if pattern[j] == text[i]
      i += 1
      j += 1
    end
    
    if j == pattern.length
      matches << i - j
      j = lps[j - 1]
    elsif i < text.length && pattern[j] != text[i]
      j != 0 ? j = lps[j - 1] : i += 1
    end
  end
  matches
end

puts kmp_search("ABABDABACDABABCABCABCABCABC", "ABABCABCABCABC").inspect""")

    # Clojure
    with open(f"{base_dir}/kmp_algorithm.clj", "w") as f:
        f.write("""(defn compute-lps [pattern]
  (loop [lps (vec (repeat (count pattern) 0))
         len 0
         i 1]
    (cond
      (>= i (count pattern)) lps
      (= (nth pattern i) (nth pattern len))
      (recur (assoc lps i (inc len)) (inc len) (inc i))
      (not= len 0)
      (recur lps (nth lps (dec len)) i)
      :else
      (recur (assoc lps i 0) len (inc i)))))

(defn kmp-search [text pattern]
  (let [lps (compute-lps pattern)]
    (loop [i 0 j 0 matches []]
      (cond
        (>= i (count text)) matches
        (= (nth pattern j) (nth text i))
        (let [new-i (inc i) new-j (inc j)]
          (if (= new-j (count pattern))
            (recur new-i (nth lps (dec new-j)) (conj matches (- new-i new-j)))
            (recur new-i new-j matches)))
        (and (< i (count text)) (not= (nth pattern j) (nth text i)))
        (if (not= j 0)
          (recur i (nth lps (dec j)) matches)
          (recur (inc i) j matches))
        :else matches))))

(println (kmp-search "ABABDABACDABABCABCABCABCABC" "ABABCABCABCABC"))""")

def complete_remaining_placeholders():
    """Completa placeholders restantes em várias linguagens"""
    
    # Longest Common Subsequence - Ruby e Clojure
    base_dir = "/Users/vitorh/Documents/GIthub/algorithms/longest-common-subsequence"
    
    with open(f"{base_dir}/lcs.rb", "w") as f:
        f.write("""def lcs(str1, str2)
  m, n = str1.length, str2.length
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  
  (1..m).each do |i|
    (1..n).each do |j|
      if str1[i-1] == str2[j-1]
        dp[i][j] = dp[i-1][j-1] + 1
      else
        dp[i][j] = [dp[i-1][j], dp[i][j-1]].max
      end
    end
  end
  
  dp[m][n]
end

puts lcs("ABCDGH", "AEDFHR")""")

    with open(f"{base_dir}/lcs.clj", "w") as f:
        f.write("""(defn lcs [str1 str2]
  (let [m (count str1)
        n (count str2)
        dp (vec (for [i (range (inc m))]
                 (vec (repeat (inc n) 0))))]
    (reduce (fn [dp i]
             (reduce (fn [dp j]
                      (if (= (nth str1 (dec i)) (nth str2 (dec j)))
                        (assoc-in dp [i j] (inc (get-in dp [(dec i) (dec j)])))
                        (assoc-in dp [i j] (max (get-in dp [(dec i) j])
                                               (get-in dp [i (dec j)])))))
                    dp (range 1 (inc n))))
           dp (range 1 (inc m)))
    (get-in dp [m n])))

(println (lcs "ABCDGH" "AEDFHR"))""")

if __name__ == "__main__":
    print("Completando algoritmos de string e matemáticos...")
    complete_palindrome()
    complete_kmp_algorithm()
    complete_remaining_placeholders()
    print("Algoritmos de string e matemáticos completados!")
