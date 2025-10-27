function isPalindromeSimple(s: string): boolean {
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
console.log(isPalindromeClean("race a car"));