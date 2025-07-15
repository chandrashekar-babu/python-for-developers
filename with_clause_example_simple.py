# Traditional approach
file = open('example.txt', 'w')
try:
    file.write('Hello, world!')
finally:
    file.close()

# With context manager
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
# File is automatically closed when exiting the block
