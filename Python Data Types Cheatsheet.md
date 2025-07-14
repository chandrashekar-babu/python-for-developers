# Python Data Types Cheatsheet

## 1. Integers (`int`)

**Description**: Whole numbers, positive or negative, without a decimal point.

**Usage Example**:
```python
age = 30
negative_num = -100
big_num = 12345678901234567890
```

**Useful Methods**: Integers don't have many specific methods, as they are immutable.
- `int.bit_length()`: Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.

**Supported Operators**:
- Arithmetic: `+`, `-`, `*`, `/` (float division), `//` (integer division), `%` (modulo), `**` (exponentiation)
- Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Bitwise: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

**Conversion Mechanisms**:
- To float: `float(integer_var)`
- To str: `str(integer_var)`
- From float (truncates decimal): `int(float_var)`
- From str (must contain only digits, optionally a sign): `int(string_var)`

## 2. Floats (`float`)

**Description**: Real numbers, positive or negative, containing one or more decimal points.

**Usage Example**:
```python
price = 19.99
pi = 3.14159
scientific_notation = 1.23e-5  # 0.0000123
```

**Useful Methods**: Floats don't have many specific methods.
- `float.as_integer_ratio()`: Returns a pair of integers whose ratio is exactly equal to the float.
- `float.is_integer()`: Returns `True` if the float value is finite with a zero fractional part, and `False` otherwise.

**Supported Operators**:
- Arithmetic: `+`, `-`, `*`, `/`, `//` (float division, result is float), `%`, `**`
- Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`

**Conversion Mechanisms**:
- To int (truncates decimal): `int(float_var)`
- To str: `str(float_var)`
- From int: `float(integer_var)`
- From str (must represent a valid number): `float(string_var)`

## 3. Strings (`str`)

**Description**: Immutable sequences of Unicode characters.

**Usage Example**:
```python
name = "Alice"
message = 'Hello, World!'
multiline_string = """This is a
multi-line string."""
```

**Useful Methods**: (Many more available!)
- `len(string_var)`: Returns the length of the string.
- `str.lower()`, `str.upper()`: Convert case.
- `str.strip()`, `str.lstrip()`, `str.rstrip()`: Remove leading/trailing whitespace (or specified characters).
- `str.split(delimiter)`: Split string into a list of substrings.
- `str.join(list_of_strings)`: Join elements of an iterable with the string as a separator.
- `str.find(substring)`, `str.index(substring)`: Find first occurrence of a substring.
- `str.replace(old, new)`: Replace occurrences of a substring.
- `str.startswith(prefix)`, `str.endswith(suffix)`: Check start/end.
- `str.isalpha()`, `str.isdigit()`, `str.isalnum()`: Check character types.
- `str.format(...)`, f-strings: String formatting.

**Supported Operators**:
- Concatenation: `+`
- Repetition: `*` (with an integer)
- Membership: `in`, `not in` (checks for substring)
- Indexing: `string_var[index]` (e.g., `name[0]` is `'A'`)
- Slicing: `string_var[start:end:step]` (e.g., `name[1:3]` is `'li'`)

**Conversion Mechanisms**:
- To list (of characters): `list(string_var)`
- To int (if numeric string): `int(string_var)`
- To float (if numeric string): `float(string_var)`
- From most other types: `str(other_type_var)`

## 4. Booleans (`bool`)

**Description**: Represents truth values: `True` or `False`. Subclass of `int` (where `True` is 1, `False` is 0).

**Usage Example**:
```python
is_active = True
has_permission = False
result = (5 > 3)  # True
```

**Useful Methods**: None specific, as they are simple values.

**Supported Operators**:
- Logical: `and`, `or`, `not`
- Comparison: `==`, `!=`
- Arithmetic: Can be used in arithmetic operations (e.g., `True + True` is 2).

**Conversion Mechanisms**:
- To int: `int(True)` is 1, `int(False)` is 0.
- To str: `str(True)` is `'True'`.
- From other types (`bool()`):
  - `bool(0)`, `bool(0.0)`, `bool("")`, `bool([])`, `bool({})`, `bool(set())`, `bool(None)` are `False`.
  - All other non-empty/non-zero values are `True`.

## 5. Lists (`list`)

**Description**: Mutable, ordered sequences of items. Items can be of different data types.

**Usage Example**:
```python
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]
empty_list = []
```

**Useful Methods**:
- `len(list_var)`: Returns the number of items.
- `list.append(item)`: Add item to the end.
- `list.insert(index, item)`: Insert item at a specific index.
- `list.extend(iterable)`: Extend list by appending elements from an iterable.
- `list.remove(item)`: Remove first occurrence of item by value.
- `list.pop(index)`: Remove and return item at index (default last).
- `list.index(item)`: Return index of first occurrence of item.
- `list.count(item)`: Return number of times item appears.
- `list.sort()`: Sorts the list in-place.
- `list.reverse()`: Reverses the list in-place.
- `list.copy()`: Returns a shallow copy.
- `list.clear()`: Removes all items.

**Supported Operators**:
- Concatenation: `+`
- Repetition: `*` (with an integer)
- Membership: `in`, `not in`
- Indexing: `list_var[index]`
- Slicing: `list_var[start:end:step]`

**Conversion Mechanisms**:
- To tuple: `tuple(list_var)`
- To set: `set(list_var)` (removes duplicates)
- From str (creates list of characters): `list(string_var)`
- From tuple, set, dict (keys only): `list(iterable_var)`

## 6. Tuples (`tuple`)

**Description**: Immutable, ordered sequences of items. Items can be of different data types.

**Usage Example**:
```python
coordinates = (10, 20)
person_info = ("John Doe", 30, "Software Engineer")
single_item_tuple = (5,)  # Comma is crucial for single-item tuples
empty_tuple = ()
```

**Useful Methods**: (Fewer than lists due to immutability)
- `len(tuple_var)`: Returns the number of items.
- `tuple.index(item)`: Return index of first occurrence of item.
- `tuple.count(item)`: Return number of times item appears.

**Supported Operators**:
- Concatenation: `+`
- Repetition: `*` (with an integer)
- Membership: `in`, `not in`
- Indexing: `tuple_var[index]`
- Slicing: `tuple_var[start:end:step]`

**Conversion Mechanisms**:
- To list: `list(tuple_var)`
- To set: `set(tuple_var)` (removes duplicates)
- From list, str, set, dict (keys only): `tuple(iterable_var)`

## 7. Dictionaries (`dict`)

**Description**: Mutable, unordered (pre-Python 3.7) / ordered (Python 3.7+ insertion order guaranteed) collections of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples).

**Usage Example**:
```python
person = {"name": "Alice", "age": 25, "city": "New York"}
empty_dict = {}
```

**Useful Methods**:
- `len(dict_var)`: Returns the number of key-value pairs.
- `dict_var[key]`: Access value by key (raises KeyError if key not found).
- `dict_var.get(key, default_value)`: Get value by key, returns `None` or `default_value` if key not found.
- `dict_var[key] = value`: Add or update a key-value pair.
- `dict_var.pop(key)`: Remove item with specified key and return its value.
- `dict_var.keys()`: Returns a view object of all keys.
- `dict_var.values()`: Returns a view object of all values.
- `dict_var.items()`: Returns a view object of all key-value pairs as tuples.
- `dict_var.update(other_dict)`: Update dictionary with key-value pairs from another dictionary.
- `dict_var.clear()`: Remove all items.

**Supported Operators**:
- Membership: `in`, `not in` (checks for key presence)

**Conversion Mechanisms**:
- From list of 2-item tuples: `dict([('a', 1), ('b', 2)])`
- From keyword arguments: `dict(name='Alice', age=25)`
- To list (of keys): `list(dict_var)`
- To list (of values): `list(dict_var.values())`
- To list (of items): `list(dict_var.items())`

## 8. Sets (`set`)

**Description**: Mutable, unordered collections of unique, immutable items.

**Usage Example**:
```python
unique_numbers = {1, 2, 3, 2, 4}  # {1, 2, 3, 4}
vowels = {'a', 'e', 'i', 'o', 'u'}
empty_set = set()  # Use set() for empty set, not {} which creates an empty dict
```

**Useful Methods**:
- `len(set_var)`: Returns the number of items.
- `set.add(item)`: Add an item.
- `set.remove(item)`: Remove item (raises KeyError if not found).
- `set.discard(item)`: Remove item if present (no error if not found).
- `set.pop()`: Remove and return an arbitrary item.
- `set.clear()`: Remove all items.
- `set.union(other_set)` or `set1 | set2`: All unique items from both sets.
- `set.intersection(other_set)` or `set1 & set2`: Common items.
- `set.difference(other_set)` or `set1 - set2`: Items in set1 but not set2.
- `set.symmetric_difference(other_set)` or `set1 ^ set2`: Items in either set, but not both.
- `set.issubset(other_set)`, `set.issuperset(other_set)`, `set.isdisjoint(other_set)`: Relationship checks.

**Supported Operators**:
- Membership: `in`, `not in`
- Set Operations: `|`, `&`, `-`, `^` (union, intersection, difference, symmetric difference)

**Conversion Mechanisms**:
- To list: `list(set_var)`
- To tuple: `tuple(set_var)`
- From list, tuple, str (creates set of characters), dict (creates set of keys): `set(iterable_var)`
