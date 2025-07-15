def countdown(start):
    while start > 0:
        yield start
        start -= 1

# Usage
for i in countdown(5):
    print(i)  # 5, 4, 3, 2, 1

# We can also get the generator manually
gen = countdown(3)
print(next(gen))  # 3
print(next(gen))  # 2
print(next(gen))  # 1
# next(gen)  # Raises StopIteration
