function gcd(a, b) {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

function gcdRecursive(a, b) {
    if (b === 0) return a;
    return gcdRecursive(b, a % b);
}

function lcm(a, b) {
    return Math.abs(a * b) / gcd(a, b);
}

function extendedGcd(a, b) {
    if (a === 0) {
        return [b, 0, 1];
    }
    
    const [gcdVal, x1, y1] = extendedGcd(b % a, a);
    const x = y1 - Math.floor(b / a) * x1;
    const y = x1;
    
    return [gcdVal, x, y];
}

// Test
console.log(`GCD(48, 18) = ${gcd(48, 18)}`); // 6
console.log(`LCM(48, 18) = ${lcm(48, 18)}`); // 144
