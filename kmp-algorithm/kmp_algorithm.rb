def compute_lps(pattern)
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

puts kmp_search("ABABDABACDABABCABCABCABCABC", "ABABCABCABCABC").inspect