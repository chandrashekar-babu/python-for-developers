# Python Functions Cheatsheet

## 1. Function Definition (`def`)

**Description**: Functions are blocks of organized, reusable code that perform a single, related action. They help break down programs into smaller, modular chunks, making code more manageable, readable, and reusable.

**Syntax**:
```python
def function_name(parameter1, parameter2, ...):
    """
    Docstring: A brief description of what the function does.
    """
    # Function body: code to be executed
    # ...
    return result  # Optional: return a value
```

**Key Points**:
- `def` keyword: Used to define a function
- `function_name`: A unique identifier for the function (follows Python naming conventions, typically lowercase with underscores)
- `parameters`: Variables listed inside the parentheses. They are placeholders for the values (arguments) the function will receive when called. Optional.
- `:` (colon): Marks the end of the function header
- Indentation: The function body must be indented (typically 4 spaces) to indicate its scope
- Docstring: An optional string literal (enclosed in triple quotes) that explains the function's purpose. Good practice for documentation.

**Usage Example**:
```python
def greet(name):
    """This function greets the person passed in as a name."""
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function
greet("Bob")
```

## 2. Arguments

**Description**: Values passed into a function when it is called. Python supports several types of arguments.

### 2.1. Positional Arguments

**Description**: Arguments passed to a function in the correct positional order. The order matters.

**Usage Example**:
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # 5 is assigned to 'a', 3 to 'b'
print(result)  # Output: 8

# Order matters:
result_wrong_order = add_numbers("Hello", "World")
print(result_wrong_order)  # Output: HelloWorld
```

### 2.2. Keyword Arguments

**Description**: Arguments identified by their parameter name when passed to the function. The order does not matter.

**Usage Example**:
```python
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person(name="Alice", age=30, city="New York")
describe_person(city="London", name="Bob", age=25)  # Order doesn't matter
```

**Mixing Positional and Keyword**: Positional arguments must come before keyword arguments.
```python
def mixed_args(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

mixed_args(10, c=30, b=20)  # Valid: 10 (pos), c=30 (kw), b=20 (kw)
# mixed_args(a=10, 20, 30)  # INVALID: Positional argument after keyword argument
```

### 2.3. Default Arguments

**Description**: Parameters that have a default value assigned in the function definition. If an argument for that parameter is not provided during the call, the default value is used.

**Usage Example**:
```python
def power(base, exponent=2):  # exponent has a default value of 2
    return base ** exponent

print(power(5))        # Output: 25 (5^2)
print(power(5, 3))     # Output: 125 (5^3)
print(power(base=2, exponent=4))  # Output: 16
```

**Key Point**: Default arguments must be defined after non-default arguments.

### 2.4. Variable-Length Arguments (`*args` and `**kwargs`)

**Description**: Allow a function to accept an arbitrary number of arguments.

#### `*args` (Arbitrary Positional Arguments)

**Description**: Collects an arbitrary number of positional arguments into a tuple.

**Usage Example**:
```python
def sum_all_numbers(*numbers):  # 'numbers' will be a tuple
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all_numbers(1, 2, 3))          # Output: 6
print(sum_all_numbers(10, 20, 30, 40))   # Output: 100
print(sum_all_numbers())                  # Output: 0
```

#### `**kwargs` (Arbitrary Keyword Arguments)

**Description**: Collects an arbitrary number of keyword arguments into a dictionary.

**Usage Example**:
```python
def display_info(**details):  # 'details' will be a dictionary
    for key, value in details.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

display_info(name="Charlie", age=35, occupation="Developer")
# Output:
# Name: Charlie
# Age: 35
# Occupation: Developer

display_info(product="Laptop", price=1200, brand="TechCo")
```

**Order of Arguments**: When combining all types, the order is:
1. Standard positional arguments
2. Default arguments
3. `*args`
4. `**kwargs`

```python
def complex_function(a, b=1, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

complex_function(10, 20, 30, 40, name="Alice", city="Wonderland")
# Output:
# a: 10, b: 20
# args: (30, 40)
# kwargs: {'name': 'Alice', 'city': 'Wonderland'}
```

## 3. `return` Statement

**Description**: Used to exit a function and optionally send a value back to the caller.

**Syntax**:
```python
return [expression]
```

**Key Points**:
- When `return` is executed, the function immediately stops, and control is passed back to the point where the function was called
- If no `return` statement is present, or if `return` is used without an expression, the function implicitly returns `None`
- A function can return any Python object (numbers, strings, lists, tuples, dictionaries, other functions, etc.)
- Functions can return multiple values by returning a tuple (which is unpacked by the caller)

**Usage Examples**:
```python
# Returning a single value
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print(product)  # Output: 24

# Function implicitly returning None
def do_nothing():
    pass  # This function does nothing and implicitly returns None

result_none = do_nothing()
print(result_none)  # Output: None

# Returning multiple values (as a tuple)
def get_min_max(numbers):
    if not numbers:
        return None, None  # Return two None values if list is empty
    return min(numbers), max(numbers)

data = [10, 5, 20, 15]
minimum, maximum = get_min_max(data)  # Unpacking the returned tuple
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 5, Max: 20

# Using return to exit early
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Return the first even number found
    return None  # If no even number is found

print(find_first_even([1, 3, 5, 8, 9]))  # Output: 8
print(find_first_even([1, 3, 5, 7]))     # Output: None
```