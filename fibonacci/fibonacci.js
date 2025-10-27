function fibonacciRecursive(n) {
    if (n <= 1) return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

function fibonacciIterative(n) {
    if (n <= 1) return n;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, a + b];
    }
    return b;
}

const fibonacciMemoized = (function() {
    const memo = {};
    return function(n) {
        if (n in memo) return memo[n];
        if (n <= 1) return n;
        return memo[n] = fibonacciMemoized(n - 1) + fibonacciMemoized(n - 2);
    };
})();

console.log("Recursive:", fibonacciRecursive(10));
console.log("Iterative:", fibonacciIterative(10));
console.log("Memoized:", fibonacciMemoized(10));