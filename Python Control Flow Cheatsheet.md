# Python Control Flow Cheatsheet

## 1. Conditional Statements: `if`, `elif`, `else`

**Description**: Used to execute different blocks of code based on whether a condition is `True` or `False`.

**Syntax**:
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition1 is False AND condition2 is True
else:
    # Code to execute if all preceding conditions are False
```

**Key Points**:
- `if` is mandatory.
- `elif` (else if) is optional and can be used multiple times.
- `else` is optional and catches all cases not covered by `if` or `elif`.
- Conditions are evaluated in order. The first `True` condition's block is executed, and the rest are skipped.
- Indentation (4 spaces or 1 tab by convention) defines code blocks.

**Usage Examples**:
```python
# Simple if
age = 18
if age >= 18:
    print("You are an adult.")

# if-else
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# if-elif-else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Nested if
is_logged_in = True
is_admin = False
if is_logged_in:
    print("Welcome, user!")
    if is_admin:
        print("You have admin privileges.")
    else:
        print("You do not have admin privileges.")
```

## 2. Looping: `for` loops

**Description**: Used to iterate over a sequence (like a list, tuple, string, dictionary, or range) or other iterable objects.

**Syntax**:
```python
for item in iterable:
    # Code to execute for each item
```

**Key Points**:
- The loop continues until all items in the iterable have been processed.
- `break`: Terminates the loop entirely.
- `continue`: Skips the rest of the current iteration and moves to the next item.
- `else` clause (optional): Executes if the loop completes without encountering a `break` statement.

**Usage Examples**:
```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterating using range()
# range(stop) -> 0 to stop-1
# range(start, stop) -> start to stop-1
# range(start, stop, step)
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Count: {i}")

# Iterating over a string
word = "Python"
for char in word:
    print(char)

# Iterating over a dictionary (keys by default)
student = {"name": "Alice", "age": 20, "major": "CS"}
for key in student:
    print(f"Key: {key}, Value: {student[key]}")

# Iterating over dictionary items (key-value pairs)
for key, value in student.items():
    print(f"{key}: {value}")

# for loop with break
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Found 3, breaking loop.")
        break
    print(num)

# for loop with continue
for i in range(1, 6):
    if i % 2 == 0:
        print(f"Skipping even number: {i}")
        continue
    print(f"Odd number: {i}")

# for loop with else
for i in range(3):
    print(f"Loop iteration {i}")
else:
    print("Loop finished normally.")

# Example where else is not executed
for i in range(3):
    print(f"Loop iteration {i}")
    if i == 1:
        break
else:
    print("This will NOT print if break is hit.")
```

## 3. Looping: `while` loops

**Description**: Used to repeatedly execute a block of code as long as a given condition is `True`.

**Syntax**:
```python
while condition:
    # Code to execute as long as condition is True
```

**Key Points**:
- The condition is checked at the beginning of each iteration. If it becomes `False`, the loop terminates.
- **Infinite Loops**: Be careful to ensure the condition eventually becomes `False` to avoid infinite loops.
- `break`: Terminates the loop entirely.
- `continue`: Skips the rest of the current iteration and moves back to check the condition.
- `else` clause (optional): Executes if the loop completes normally (i.e., the condition becomes `False`) without encountering a `break` statement.

**Usage Examples**:
```python
# Simple while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Important: increment to avoid infinite loop

# while loop with break
secret_number = 7
guess = 0
while True:  # Infinite loop until broken
    guess = int(input("Guess the secret number (1-10): "))
    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break
    else:
        print("Try again!")

# while loop with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        print(f"Skipping even number {num}")
        continue
    print(f"Odd number {num}")

# while loop with else
x = 0
while x < 3:
    print(f"While loop iteration {x}")
    x += 1
else:
    print("While loop finished normally.")

# Example where else is not executed
y = 0
while y < 5:
    print(f"While loop iteration {y}")
    if y == 2:
        break
    y += 1
else:
    print("This will NOT print if break is hit.")
```