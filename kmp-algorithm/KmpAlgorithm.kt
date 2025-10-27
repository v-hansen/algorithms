fun computeLPS(pattern: String): IntArray {
    val m = pattern.length
    val lps = IntArray(m)
    var length = 0
    var i = 1
    
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++
            lps[i] = length
            i++
        } else {
            if (length != 0) {
                length = lps[length - 1]
            } else {
                lps[i] = 0
                i++
            }
        }
    }
    return lps
}

fun kmpSearch(text: String, pattern: String): List<Int> {
    val n = text.length
    val m = pattern.length
    
    if (m == 0) return emptyList()
    
    val lps = computeLPS(pattern)
    val matches = mutableListOf<Int>()
    
    var i = 0
    var j = 0
    while (i < n) {
        if (pattern[j] == text[i]) {
            i++
            j++
        }
        
        if (j == m) {
            matches.add(i - j)
            j = lps[j - 1]
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1]
            } else {
                i++
            }
        }
    }
    
    return matches
}

fun main() {
    val text = "ABABDABACDABABCABCABCABCABC"
    val pattern = "ABABCABCABCABC"
    val matches = kmpSearch(text, pattern)
    println("Pattern found at indices: $matches")
}
