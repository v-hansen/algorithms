def gcd(a, b):
    """Greatest Common Divisor using Euclidean Algorithm"""
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    """Recursive version"""
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a, b):
    """Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd_val, x, y

# Test
print(f"GCD(48, 18) = {gcd(48, 18)}")  # 6
print(f"LCM(48, 18) = {lcm(48, 18)}")  # 144
