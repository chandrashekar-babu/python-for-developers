# Syntax
# {key_expr: value_expr for item in iterable if condition}

# Example: Map numbers to their squares
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering example
even_square_dict = {x: x**2 for x in range(10) if x % 2 == 0}