# Python Data Model Methods ("Dunder Methods") Cheatsheet

Python's data model methods (with double underscores) allow custom objects to integrate with built-in operations and operators.

## 1. Arithmetic Operators

```python
__add__(self, other)      # + (addition)
__sub__(self, other)      # - (subtraction)
__mul__(self, other)      # * (multiplication)
__truediv__(self, other)  # / (true division)
__floordiv__(self, other) # // (floor division)
__mod__(self, other)      # % (modulo)
__pow__(self, other)      # ** (exponentiation)
```

**Example**:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 3)
v2 = Vector(1, 5)
print(v1 + v2)  # Vector(3, 8)
print(v1 * 3)   # Vector(6, 9)
```

## 2. Comparison Operators

```python
__eq__(self, other)  # == (equality)
__ne__(self, other)  # != (inequality)
__lt__(self, other)  # < (less than)
__le__(self, other)  # <= (less than or equal)
__gt__(self, other)  # > (greater than)
__ge__(self, other)  # >= (greater than or equal)
```

**Example**:
```python
class Point:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x + self.y) < (other.x + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 == p2)  # False
print(p1 < p2)   # True
```

## 3. Container Methods

```python
__len__(self)          # len(obj)
__getitem__(self, key) # obj[key]
__setitem__(self, key, value) # obj[key] = value
__delitem__(self, key) # del obj[key]
__contains__(self, item) # item in obj
```

**Example**:
```python
class CustomList:
    def __len__(self):
        return len(self._data)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __contains__(self, item):
        return item in self._data

my_list = CustomList([1, 2, 3])
print(len(my_list))  # 3
print(my_list[1])    # 2
print(3 in my_list)  # True
```

## 4. Callable Objects

```python
__call__(self, *args, **kwargs) # Makes instance callable
```

**Example**:
```python
class Multiplier:
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))  # 10
```

## 5. String Representation

```python
__str__(self)   # str(obj), print(obj) - human-readable
__repr__(self)  # repr(obj) - unambiguous, for debugging
```

**Example**:
```python
class Book:
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"
```

## 6. Context Managers

```python
__enter__(self)  # with obj as x:
__exit__(self, exc_type, exc_val, exc_tb) # Cleanup
```

**Example**:
```python
class Timer:
    def __enter__(self):
        self.start = time.time()
    
    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start}")
```

## 7. Attribute Access

```python
__getattr__(self, name)  # obj.undefined_attr
__setattr__(self, name, value) # obj.attr = value
__delattr__(self, name)  # del obj.attr
```

**Example**:
```python
class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute {name} not found"
```

## 8. Numeric Type Emulation

```python
__abs__(self)    # abs(obj)
__int__(self)    # int(obj)
__float__(self)  # float(obj)
__round__(self)  # round(obj)
```

## 9. Iterator Protocol

```python
__iter__(self)  # iter(obj)
__next__(self)  # next(obj)
```

**Example**:
```python
class Countdown:
    def __iter__(self):
        self.value = self.start
        return self
    
    def __next__(self):
        if self.value < 0:
            raise StopIteration
        current = self.value
        self.value -= 1
        return current
```

## 10. Descriptors

```python
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
```

This cheatsheet covers the essential special methods that enable your objects to:
- Support arithmetic operations
- Handle comparisons
- Act like containers
- Become callable
- Customize string representation
- Work with context managers
- Control attribute access
- Emulate numeric types
- Implement iteration
- Create descriptors
