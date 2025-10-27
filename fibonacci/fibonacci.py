def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_sequence(n):
    """
    Recursively prints the Fibonacci sequence up to the nth term.

    This function uses a recursive approach to generate Fibonacci numbers
    and prints each number in the sequence up to the nth term.

    Args:
    n (int): The number of terms in the Fibonacci sequence to print.
             Must be a non-negative integer.

    Returns:
    None: This function prints the sequence but does not return any value.

    Raises:
    ValueError: If n is negative.

    Example:
    >>> print_fibonacci_sequence(5)
    0
    1
    1
    2
    3
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0:
        return
    
    print_fibonacci_sequence(n - 1)
    print(fibonacci(n - 1)) 