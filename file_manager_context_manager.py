class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to let exceptions propagate
        # Return True to suppress exceptions
        return False

# Usage
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')
