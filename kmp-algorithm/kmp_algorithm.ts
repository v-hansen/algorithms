function computeLPS(pattern: string): number[] {
    const m = pattern.length;
    const lps: number[] = new Array(m).fill(0);
    let length = 0;
    let i = 1;
    
    while (i < m) {
        if (pattern[i] === pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length !== 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

function kmpSearch(text: string, pattern: string): number[] {
    const n = text.length;
    const m = pattern.length;
    
    if (m === 0) return [];
    
    const lps = computeLPS(pattern);
    const matches: number[] = [];
    
    let i = 0, j = 0;
    while (i < n) {
        if (pattern[j] === text[i]) {
            i++;
            j++;
        }
        
        if (j === m) {
            matches.push(i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] !== text[i]) {
            if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    
    return matches;
}

// Test
const text = "ABABDABACDABABCABCABCABCABC";
const pattern = "ABABCABCABCABC";
const matches = kmpSearch(text, pattern);
console.log(`Pattern found at indices: ${matches}`);
