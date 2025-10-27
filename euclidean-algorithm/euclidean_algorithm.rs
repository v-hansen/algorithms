fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a
}

fn gcd_recursive(a: i32, b: i32) -> i32 {
    if b == 0 { a } else { gcd_recursive(b, a % b) }
}

fn lcm(a: i32, b: i32) -> i32 {
    (a * b) / gcd(a, b)
}

fn extended_gcd(a: i32, b: i32) -> (i32, i32, i32) {
    if b == 0 {
        (a, 1, 0)
    } else {
        let (gcd, x1, y1) = extended_gcd(b, a % b);
        let x = y1;
        let y = x1 - (a / b) * y1;
        (gcd, x, y)
    }
}

fn main() {
    println!("GCD: {}", gcd(48, 18));
    println!("GCD recursive: {}", gcd_recursive(48, 18));
    println!("LCM: {}", lcm(48, 18));
    println!("Extended GCD: {:?}", extended_gcd(48, 18));
}