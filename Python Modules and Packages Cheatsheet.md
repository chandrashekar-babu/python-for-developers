# Python Modules & Packages Cheatsheet

## 1. Modules

**Description**: A module is simply a Python file (`.py`) containing Python definitions and statements. Modules allow you to logically organize your Python code, making it reusable and easier to manage.

### Creating a Module:
Save your Python code in a file with a `.py` extension.

**Example: my_module.py**
```python
# my_module.py

PI = 3.14159

def greet(name):
    return f"Hello, {name} from my_module!"

class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b

if __name__ == "__main__":
    # This code runs only when my_module.py is executed directly
    print("my_module is being run directly!")
    print(f"PI value: {PI}")
```

### Importing and Using a Module:

#### 1.1. `import module_name`
**Description**: Imports the entire module. You must use the module name as a prefix to access its contents.

**Usage Example**:
```python
# main_script.py
import my_module

print(my_module.PI)
print(my_module.greet("Alice"))

calc = my_module.Calculator()
print(calc.add(10, 5))
```

#### 1.2. `import module_name as alias`
**Description**: Imports the entire module but assigns it a shorter or more convenient alias.

**Usage Example**:
```python
# main_script.py
import my_module as mm

print(mm.PI)
print(mm.greet("Bob"))
```

#### 1.3. `from module_name import item1, item2`
**Description**: Imports specific items (functions, variables, classes) directly into the current namespace.

**Usage Example**:
```python
# main_script.py
from my_module import PI, greet, Calculator

print(PI)
print(greet("Charlie"))

calc = Calculator()
print(calc.subtract(20, 7))
```

**Caution**: Can lead to name clashes if imported items have the same name as existing variables/functions.

#### 1.4. `from module_name import item as alias`
**Description**: Imports a specific item and assigns it an alias.

**Usage Example**:
```python
# main_script.py
from my_module import greet as say_hello

say_hello("David")
```

#### 1.5. `from module_name import *`
**Description**: Imports all public items from the module directly into the current namespace.

**Caution**: Generally discouraged in production code as it can lead to name clashes.

**Usage Example**:
```python
# main_script.py
from my_module import *  # Avoid in real projects!

print(PI)
print(greet("Eve"))
```

## 2. Packages

**Description**: A package is a way of organizing related modules into a directory hierarchy. It's essentially a directory containing a special file named `__init__.py` and other module files or sub-packages.

### Creating a Package:
1. Create a directory (e.g., `my_package`)
2. Inside `my_package`, create an empty file named `__init__.py`
3. Add your modules inside this directory

**Example Structure**:
```
my_project/
├── main.py
└── my_package/
    ├── __init__.py
    ├── greetings.py
    └── calculations/
        ├── __init__.py
        └── basic_ops.py
```

**greetings.py**:
```python
# my_package/greetings.py
def say_hi(name):
    return f"Hi, {name}!"
```

**calculations/basic_ops.py**:
```python
# my_package/calculations/basic_ops.py
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### Importing and Using a Package/Sub-package/Module:

#### 2.1. Importing Modules from a Package
**Description**: You can import individual modules from within a package.

**Usage Example**:
```python
# main.py
import my_package.greetings
from my_package.calculations import basic_ops

print(my_package.greetings.say_hi("Frank"))
print(basic_ops.multiply(6, 7))
```

#### 2.2. Importing Specific Items from a Package Module
**Description**: Import specific functions/classes from a module within a package.

**Usage Example**:
```python
# main.py
from my_package.greetings import say_hi
from my_package.calculations.basic_ops import divide

print(say_hi("Grace"))
try:
    print(divide(10, 2))
    print(divide(10, 0))
except ValueError as e:
    print(e)
```

#### 2.3. Using `__init__.py`
**Description**: The `__init__.py` file is executed when a package is imported. It can be used to:
- Initialize package-level variables
- Define what happens when `from package import *` is used (by setting `__all__`)
- Make certain modules or functions directly accessible from the package level

**Example: Exposing items via `__init__.py`**
Modify `my_package/__init__.py`:
```python
# my_package/__init__.py
from .greetings import say_hi  # Relative import
from .calculations.basic_ops import multiply  # Relative import

__all__ = ["say_hi", "multiply"]  # Defines what 'from my_package import *' imports
```

Now, in `main.py`:
```python
# main.py
from my_package import say_hi, multiply  # Directly import from package

print(say_hi("Heidi"))
print(multiply(8, 9))
```

## 3. The Python Path (`sys.path`)

**Description**: When you import a module or package, Python searches for it in a list of directories defined in `sys.path`.

### Checking the Path:
```python
import sys
print(sys.path)
```

### Adding to the Path:

**Temporarily (for current session)**:
```python
import sys
sys.path.append('/path/to/your/custom/modules')
```

**Permanently**:
- Set the `PYTHONPATH` environment variable
- Install packages using `pip` (which places them in standard locations)


