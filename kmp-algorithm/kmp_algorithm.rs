fn compute_lps(pattern: &str) -> Vec<usize> {
    let pattern_bytes = pattern.as_bytes();
    let m = pattern_bytes.len();
    let mut lps = vec![0; m];
    let mut length = 0;
    let mut i = 1;
    
    while i < m {
        if pattern_bytes[i] == pattern_bytes[length] {
            length += 1;
            lps[i] = length;
            i += 1;
        } else if length != 0 {
            length = lps[length - 1];
        } else {
            lps[i] = 0;
            i += 1;
        }
    }
    lps
}

fn kmp_search(text: &str, pattern: &str) -> Vec<usize> {
    let text_bytes = text.as_bytes();
    let pattern_bytes = pattern.as_bytes();
    let n = text_bytes.len();
    let m = pattern_bytes.len();
    
    if m == 0 {
        return Vec::new();
    }
    
    let lps = compute_lps(pattern);
    let mut matches = Vec::new();
    
    let mut i = 0;
    let mut j = 0;
    
    while i < n {
        if pattern_bytes[j] == text_bytes[i] {
            i += 1;
            j += 1;
        }
        
        if j == m {
            matches.push(i - j);
            j = lps[j - 1];
        } else if i < n && pattern_bytes[j] != text_bytes[i] {
            if j != 0 {
                j = lps[j - 1];
            } else {
                i += 1;
            }
        }
    }
    
    matches
}

fn main() {
    let text = "ABABDABACDABABCABCABCABCABC";
    let pattern = "ABABCABCABCABC";
    let matches = kmp_search(text, pattern);
    println!("Pattern found at indices: {:?}", matches);
}
