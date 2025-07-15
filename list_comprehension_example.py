# Syntax
# [expression for item in iterable if condition]

# Example: Squares of even numbers from 0-9
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # [0, 4, 16, 36, 64]

# Equivalent for loop
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)