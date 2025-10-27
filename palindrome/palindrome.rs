fn is_palindrome(s: &str) -> bool {
    let cleaned: String = s.to_lowercase();
    cleaned == cleaned.chars().rev().collect::<String>()
}

fn main() {
    println!("{}", is_palindrome("racecar"));
    println!("{}", is_palindrome("hello"));
}
