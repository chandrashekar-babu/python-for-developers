class MathUtils:
    @staticmethod
    def is_prime(n):
        """Check if a number is prime"""
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
               return False
        return True
    
    @staticmethod
    def factorial(n):
        """Calculate factorial of n"""
        if n == 0 or n == 1:
            return 1
        return n * MathUtils.factorial(n-1)

# Using static methods
print(MathUtils.is_prime(17))   # True
print(MathUtils.factorial(5))   # 120