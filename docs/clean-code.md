## Uncle Bob's Clean Code Rules in Python

This guideline provides a practical approach to writing clean and maintainable Python code based on Robert C. Martin's (Uncle Bob) principles of Clean Code.

### 1. Naming

**1.1. Use Descriptive and Meaningful Names**

* **Avoid:** `x`, `y`, `data`, `temp`
* **Instead:** `customer_name`, `total_price`, `user_data`

```python
# Bad
def calculate_something(x, y):
return x * y

# Good
def calculate_product(factor1, factor2):
return factor1 * factor2
```

**1.2. Use Consistent Naming Conventions**

* **CamelCase:** for classes and methods
* **snake_case:** for variables and functions

```python
# Good
class UserAccount:
def get_username(self):
  return self.username

# Good
def calculate_total_price(products):
  total = 0
  for product in products:
  total += product.price
  return total
```

**1.3. Avoid Abbreviations**

* **Avoid:** `getNum`, `calcVal`
* **Instead:** `get_number`, `calculate_value`

**1.4. Use Prefixes for Private Members**

* `_` prefix indicates private members

```python
class User:
def __init__(self, name):
self._name = name

def get_name(self):
return self._name
```

### 2. Functions

**2.1. Keep Functions Short and Focused**

* Aim for a maximum of 5-10 lines of code per function.
* Functions should do one thing well.

```python
# Bad
def calculate_and_print_total(products):
total = 0
for product in products:
total += product.price
print(f"Total price: {total}")

# Good
def calculate_total_price(products):
total = 0
for product in products:
total += product.price
return total

def print_total_price(total):
print(f"Total price: {total}")
```

**2.2. Use Descriptive Function Names**

* Function names should clearly indicate their purpose.

```python
# Bad
def process_data(data):
# ...

# Good
def calculate_average_score(scores):
# ...
```

**2.3. Limit Parameters**

* Ideal number of parameters is 2-3.
* Use objects to pass complex data instead of multiple parameters.

```python
# Bad
def create_user(username, email, password, first_name, last_name):
# ...

# Good
class User:
def __init__(self, username, email, password, first_name, last_name):
# ...

def create_user(user):
# ...
```

**2.4. Avoid Side Effects**

* Functions should have minimal side effects on the surrounding environment.

```python
# Bad (modifies global variable)
total = 0

def add_to_total(price):
global total
total += price

# Good (returns value)
def add_to_total(total, price):
return total + price
```

### 3. Comments

**3.1. Use Comments Sparingly**

* Comments should explain *why* something is done, not *what* it does.
* Good code is self-documenting.

```python
# Bad
# This function calculates the total price
def calculate_total(products):
# ...

# Good
def calculate_total(products):
# Apply a 10% discount if the total exceeds 100
if total > 100:
return total * 0.9
return total
```

**3.2. Avoid Redundant Comments**

* Comments that simply repeat what the code does are unnecessary.

```python
# Bad
# Increment the counter
count += 1

# Good
count += 1
```

### 4. Formatting

**4.1. Consistent Indentation**

* Use 4 spaces for indentation.
* Use a consistent style for line breaks and spacing.

```python
# Good
def calculate_total(products):
total = 0
for product in products:
total += product.price
return total

# Bad
def calculate_total(products):
total = 0
for product in products:
total += product.price
return total
```

**4.2. Line Length**

* Keep lines shorter than 80 characters.
* Use line breaks and parentheses to improve readability.

```python
# Good
def calculate_total(products):
total = 0
for product in products:
total += product.price
return total

# Bad
def calculate_total(products):
total = 0
for product in products:
total += product.price
return total
```

**4.3. Use Blank Lines**

* Use blank lines to separate logical blocks of code.

```python
# Good
def calculate_total(products):
total = 0
for product in products:
total += product.price
return total

# ... other code ...

def print_total(total):
print(f"Total price: {total}")
```

### 5. Classes

**5.1. Keep Classes Small and Focused**

* Classes should have a single responsibility.
* Use inheritance to create hierarchies of classes.

```python
# Bad (too many responsibilities)
class User:
def __init__(self, username, email, password):
# ...

def create_post(self, content):
# ...

def send_message(self, recipient, message):
# ...

# Good (separate responsibilities)
class User:
def __init__(self, username, email, password):
# ...

class Post:
def __init__(self, content, author):
# ...

class Message:
def __init__(self, sender, recipient, content):
# ...
```

**5.2. Use Descriptive Class Names**

* Class names should clearly indicate their purpose.

```python
# Bad
class DataHandler:
# ...

# Good
class UserAccount:
# ...
```

**5.3. Encapsulate Data**

* Use private members and accessors to protect data.

```python
class User:
def __init__(self, name):
self._name = name

def get_name(self):
return self._name

def set_name(self, name):
self._name = name
```

**5.4. Follow the Single Responsibility Principle**

* Each class should have one specific purpose.

```python
# Bad
class UserDatabase:
def __init__(self):
# ...

def get_user(self, username):
# ...

def create_user(self, user):
# ...

def update_user(self, user):
# ...

def delete_user(self, username):
# ...

# Good
class UserDatabase:
def __init__(self):
# ...

def get_user(self, username):
# ...

class UserCreator:
def __init__(self, database):
self.database = database

def create_user(self, user):
# ...

class UserUpdater:
def __init__(self, database):
self.database = database

def update_user(self, user):
# ...

class UserDeleter:
def __init__(self, database):
self.database = database

def delete_user(self, username):
# ...
```

### 6. Error Handling

**6.1. Use Exceptions for Exceptional Cases**

* Avoid using exceptions for normal flow control.
* Use specific exception types for different error scenarios.

```python
# Bad
def divide(a, b):
if b == 0:
return "Error: Division by zero"
else:
return a / b

# Good
def divide(a, b):
if b == 0:
raise ZeroDivisionError("Division by zero")
return a / b
```

**6.2. Handle Exceptions Gracefully**

* Use `try-except` blocks to handle expected exceptions.
* Provide informative error messages.

```python
try:
result = divide(10, 0)
except ZeroDivisionError as e:
print(f"Error: {e}")
```

**6.3. Avoid Empty `except` Blocks**

* Always handle exceptions explicitly.

```python
# Bad
try:
# ...
except Exception:
pass

# Good
try:
# ...
except Exception as e:
print(f"Error: {e}")
```

### 7. Code Style

**7.1. Use a Consistent Style Guide**

* Follow the PEP 8 style guide for Python.
* Use tools like `pycodestyle` and `pylint` to check for style violations.

**7.2. Use Docstrings**

* Document classes, functions, and methods with docstrings.
* Use the Sphinx format for docstrings.

```python
def calculate_total(products):
"""Calculates the total price of a list of products.

Args:
products: A list of product objects.

Returns:
The total price of all products.
"""
total = 0
for product in products:
total += product.price
return total
```

### 8. Testing

**8.1. Write Unit Tests**

* Write tests for all critical parts of your code.
* Aim for high test coverage.

```python
import unittest

def add(a, b):
return a + b

class TestAdd(unittest.TestCase):
def test_add_positive_numbers(self):
self.assertEqual(add(2, 3), 5)

def test_add_negative_numbers(self):
self.assertEqual(add(-2, -3), -5)

def test_add_zero(self):
self.assertEqual(add(5, 0), 5)

if __name__ == '__main__':
unittest.main()
```

**8.2. Use Test-Driven Development (TDD)**

* Write tests before writing code.
* Drive development by writing failing tests and then implementing the code to pass them.

### 9. Refactoring

**9.1. Refactor Regularly**

* Refactor your code continuously to improve its structure, clarity, and efficiency.
* Use automated refactoring tools to help you with the process.

**9.2. Make Small Changes**

* Refactor in small, incremental steps.
* Test your code after each change to ensure that you don't introduce regressions.

**9.3. Avoid Code Duplication**

* Use inheritance, composition, and other techniques to avoid repeating code.

### Conclusion

Applying Uncle Bob's Clean Code principles in your Python code will lead to more readable, maintainable, and robust software. By following these guidelines and consistently practicing good coding habits, you can significantly improve the quality and longevity of your projects. Remember, writing clean code is an ongoing process that requires discipline and attention to detail. Start by choosing one or two principles to focus on and gradually incorporate more over time.
