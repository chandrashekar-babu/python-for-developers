# Python Classes and Objects Cheatsheet

## 1. Classes and Objects: Basic Concepts

- **Class**: A blueprint for creating objects. Defines attributes (data) and methods (functions).
- **Object (Instance)**: A specific instance of a class with its own state and behavior.

**OOP Principles**:
- **Encapsulation**: Bundling data and methods within a class
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Different classes responding to the same method call differently
- **Abstraction**: Hiding complex implementation details

## 2. Class Definition and Instantiation

### 2.1. Class Definition Syntax

```python
class ClassName:
    """Docstring describing the class"""
    class_variable = "Shared by all instances"
    
    def __init__(self, param1, param2):
        self.param1 = param1  # Instance variable
        self.param2 = param2  # Instance variable
    
    def instance_method(self):
        """Operates on instance data"""
        print(f"Instance method: {self.param1}")
    
    @classmethod
    def class_method(cls):
        """Operates on the class itself"""
        print(f"Class method: {cls.class_variable}")
    
    @staticmethod
    def static_method(arg):
        """Utility function, no access to instance/class"""
        print(f"Static method: {arg}")
```

**Key Points**:
- Use `class` keyword with CamelCase naming
- `__init__` is the constructor method
- `self` refers to the instance
- Class variables vs instance variables
- Method types: instance, class (`@classmethod`), static (`@staticmethod`)

### 2.2. Object Instantiation

```python
object_name = ClassName(arg1, arg2)
```

**Example**:
```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):
        return f"{self.name} says Woof!"

# Create instances
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

print(my_dog.name)    # Output: Buddy
print(your_dog.breed) # Output: Labrador
print(my_dog.bark())  # Output: Buddy says Woof!
```

## 3. Special Methods (Magic/Dunder Methods)

### 3.1. `__new__` - Object Creation
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        return super().__new__(cls)
    
    def __init__(self, value):
        print("Initializing instance")
        self.value = value
```

### 3.2. `__init__` - Object Initialization
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

### 3.3. `__del__` - Destructor
```python
class Resource:
    def __del__(self):
        print("Resource released")
```

### 3.4. `__str__` - Informal String Representation
```python
def __str__(self):
    return f"Book: {self.title} by {self.author}"
```

### 3.5. `__repr__` - Official String Representation
```python
def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"
```

### 3.6. `__bool__` - Boolean Conversion
```python
def __bool__(self):
    return len(self.items) > 0
```

## 4. Constructor Parameters

```python
class Product:
    def __init__(self, name, price, quantity=1, **details):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.details = details

# Usage
p = Product("Laptop", 1200, color="silver")
```

## 5. Inheritance

### 5.1. Basic Inheritance
```python
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

### 5.2. Using `super()`
```python
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent's __init__
        self.color = color
```

### 5.3. Method Overriding
```python
class Animal:
    def speak(self):
        return "Generic sound"

class Dog(Animal):
    def speak(self):  # Overrides parent's speak()
        return "Woof!"
```

## 6. Class Composition (Alternative to Inheritance)

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        self.engine.start()
```

## 7. Property Decorators

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        return 3.14 * self._radius ** 2
```

## 8. Abstract Base Classes (ABC)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
```

This cheatsheet covers the essential concepts of Python classes and objects, including:
- Class definition and instantiation
- Special methods
- Inheritance and polymorphism
- Composition
- Property decorators
- Abstract base classes
