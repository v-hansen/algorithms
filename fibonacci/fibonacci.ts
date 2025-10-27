function fibonacci(n: number): number {
    if (n <= 1) return n;
    
    let a = 0;
    let b = 1;
    
    for (let i = 2; i <= n; i++) {
        const temp = a + b;
        a = b;
        b = temp;
    }
    
    return b;
}

function fibonacciSequence(count: number): number[] {
    return Array.from({ length: count }, (_, i) => fibonacci(i));
}

// Exemplo de uso
console.log("Sequência de Fibonacci:");
fibonacciSequence(15).forEach((value, index) => {
    console.log(`F(${index}) = ${value}`);
});

console.log(`\nF(20) = ${fibonacci(20)}`);