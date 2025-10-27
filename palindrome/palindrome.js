function isPalindrome(str) {
    const cleaned = str.toLowerCase();
    return cleaned === cleaned.split('').reverse().join('');
}

console.log(isPalindrome("racecar"));
console.log(isPalindrome("hello"));
