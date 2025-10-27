fn is_palindrome(s: &str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    let mut left = 0;
    let mut right = chars.len() - 1;
    
    while left < right {
        if chars[left] != chars[right] {
            return false;
        }
        left += 1;
        right -= 1;
    }
    true
}

fn is_palindrome_clean(s: &str) -> bool {
    let cleaned: String = s.chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| c.to_lowercase().next().unwrap())
        .collect();
    
    cleaned == cleaned.chars().rev().collect::<String>()
}

fn main() {
    println!("{}", is_palindrome("racecar"));
    println!("{}", is_palindrome_clean("A man, a plan, a canal: Panama"));
}