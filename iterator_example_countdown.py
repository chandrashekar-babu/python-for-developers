class CountDown:
    def __init__(self, start):
        self.start = start
 
    def __iter__(self):
       # Return an iterator (CountDownIterator)
       return CountDownIterator(self.start)

class CountDownIterator:
    def __init__(self, count):
        self.count = count
 
    def __iter__(self):
        # Iterator must also be iterable, return self
        return self
 
    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        self.count -= 1
        return self.count + 1

# Usage
for i in CountDown(5):
    print(i) # 5, 4, 3, 2, 1

# We can also get the iterator manually
iterator = iter(CountDown(3))
print(next(iterator)) # 3
print(next(iterator)) # 2
print(next(iterator)) # 1
# next(iterator) # Raises StopIteration
