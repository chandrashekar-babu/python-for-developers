from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        # Code before yield is like __enter__
        file = open(filename, mode)
        yield file  # This value is returned by with ... as
    finally:
        # Code after yield is like __exit__
        file.close()

# Usage
with file_manager('example.txt', 'w') as file:
    file.write('Hello, world!')