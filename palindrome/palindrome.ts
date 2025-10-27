function isPalindrome(str: string): boolean {
    const cleaned = str.toLowerCase();
    return cleaned === cleaned.split('').reverse().join('');
}

console.log(isPalindrome("racecar"));
console.log(isPalindrome("hello"));
