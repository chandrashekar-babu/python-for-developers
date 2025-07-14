
# Python Variables & Operators Cheatsheet

## 1. Variables and Assignment

**Description**: A variable is a named location in memory used to store data. In Python, you don't declare the type of a variable explicitly; its type is inferred from the value assigned to it.

**Assignment Operator**: `=`  
Used to assign a value to a variable.

**Syntax**:
```python
variable_name = value
```

**Key Points**:
- Variable names must start with a letter or an underscore (`_`)
- They can contain letters, numbers, and underscores
- They are case-sensitive (`age` is different from `Age`)
- Keywords (like `if`, `for`, `def`) cannot be used as variable names
- Python supports dynamic typing, meaning a variable's type can change during execution

**Usage Examples**:
```python
# Assigning different data types
name = "Alice"        # String
age = 30              # Integer
height = 1.75         # Float
is_student = True     # Boolean
my_list = [1, 2, 3]   # List

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")

# Reassigning a variable (type can change)
x = 10
print(f"x initially: {x}, Type: {type(x)}")
x = "Hello"
print(f"x after reassign: {x}, Type: {type(x)}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# Assigning the same value to multiple variables
x = y = z = 0
print(f"x: {x}, y: {y}, z: {z}")
```

## 2. Arithmetic Operators

**Description**: Used to perform mathematical calculations.

**Operators**:
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division (always returns a float)
- `//` : Floor Division (returns integer part of the quotient)
- `%` : Modulo (returns the remainder of the division)
- `**` : Exponentiation (power)

**Usage Examples**:
```python
num1 = 15
num2 = 4

# Addition
print(f"{num1} + {num2} = {num1 + num2}")  # Output: 19

# Subtraction
print(f"{num1} - {num2} = {num1 - num2}")  # Output: 11

# Multiplication
print(f"{num1} * {num2} = {num1 * num2}")  # Output: 60

# Division (float result)
print(f"{num1} / {num2} = {num1 / num2}")  # Output: 3.75

# Floor Division (integer result)
print(f"{num1} // {num2} = {num1 // num2}")  # Output: 3

# Modulo (remainder)
print(f"{num1} % {num2} = {num1 % num2}")  # Output: 3 (15 = 3*4 + 3)

# Exponentiation
print(f"{num1} ** 2 = {num1 ** 2}")  # Output: 225 (15 squared)
print(f"2 ** 3 = {2 ** 3}")           # Output: 8 (2 cubed)

# Combined Assignment Operators (e.g., `+=`, `-=`, `*=`, `/=`, etc.)
x = 10
x += 5  # Equivalent to x = x + 5
print(f"x after x += 5: {x}")  # Output: 15

y = 20
y /= 4  # Equivalent to y = y / 4
print(f"y after y /= 4: {y}")  # Output: 5.0
```

## 3. Comparison Operators

**Description**: Used to compare two values. They always return a Boolean value (`True` or `False`).

**Operators**:
- `==` : Equal to
- `!=` : Not equal to
- `>` : Greater than
- `<` : Less than
- `>=` : Greater than or equal to
- `<=` : Less than or equal to

**Usage Examples**:
```python
a = 10
b = 20
c = 10

# Equal to
print(f"a == b: {a == b}")  # Output: False
print(f"a == c: {a == c}")  # Output: True

# Not equal to
print(f"a != b: {a != b}")  # Output: True

# Greater than
print(f"b > a: {b > a}")    # Output: True

# Less than
print(f"a < b: {a < b}")    # Output: True

# Greater than or equal to
print(f"a >= c: {a >= c}")  # Output: True
print(f"b >= a: {b >= a}")  # Output: True

# Less than or equal to
print(f"a <= c: {a <= c}")  # Output: True
print(f"a <= b: {a <= b}")  # Output: True

# Comparing strings
str1 = "apple"
str2 = "banana"
print(f"str1 == str2: {str1 == str2}")  # Output: False
print(f"str1 < str2: {str1 < str2}")    # Output: True (lexicographical comparison)
```

## 4. Logical Operators

**Description**: Used to combine conditional statements. They operate on Boolean values and return a Boolean value.

**Operators**:
- `and` : Returns `True` if both operands are `True`
- `or` : Returns `True` if at least one of the operands is `True`
- `not` : Reverses the Boolean state of the operand

**Key Points**:
- **Short-circuiting**:
  - `and`: If the first operand is `False`, the second operand is not evaluated
  - `or`: If the first operand is `True`, the second operand is not evaluated
- Logical operators can return the actual values of the operands, not just `True`/`False`, depending on which operand determines the result

**Usage Examples**:
```python
is_sunny = True
is_warm = False
has_umbrella = False

# 'and' operator
print(f"Is it sunny AND warm? {is_sunny and is_warm}")  # Output: False
print(f"True and True: {True and True}")              # Output: True

# 'or' operator
print(f"Is it sunny OR warm? {is_sunny or is_warm}")    # Output: True
print(f"False or False: {False or False}")            # Output: False

# 'not' operator
print(f"Not sunny: {not is_sunny}")            # Output: False
print(f"Not has_umbrella: {not has_umbrella}")  # Output: True

# Combining operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("Eligible to drive.")
else:
    print("Not eligible to drive.")

# Short-circuiting example
def check_true():
    print("check_true evaluated")
    return True

def check_false():
    print("check_false evaluated")
    return False

print("\nShort-circuiting 'and':")
result_and = check_false() and check_true()  # check_true() is not called
print(f"Result: {result_and}")

print("\nShort-circuiting 'or':")
result_or = check_true() or check_false()  # check_false() is not called
print(f"Result: {result_or}")
```
