# Syntax
# {expression for item in iterable if condition}

# Example: Set of unique letters in a string
letters = {char.lower() for char in "Hello World" if char.isalpha()}
print(letters)  # {'e', 'd', 'h', 'l', 'o', 'r', 'w'}