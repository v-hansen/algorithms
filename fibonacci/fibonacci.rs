fn fibonacci(n: u32) -> u64 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a = 0u64;
            let mut b = 1u64;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}

fn fibonacci_sequence(count: u32) -> Vec<u64> {
    (0..count).map(|i| fibonacci(i)).collect()
}

fn main() {
    println!("Sequência de Fibonacci:");
    for (i, value) in fibonacci_sequence(15).iter().enumerate() {
        println!("F({}) = {}", i, value);
    }
    
    println!("\nF(20) = {}", fibonacci(20));
}