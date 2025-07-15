def is_prime(n):
    """Check if n is a prime number"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Returns factorial of n"""
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


