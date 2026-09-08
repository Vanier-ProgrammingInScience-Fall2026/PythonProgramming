# Lecture 3: Built-in Functions

### **Table of Contents**

- [Lecture 3: Built-in Functions](#lecture-3-built-in-functions)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Python Built-In Functions, Packages, and Modules**](#1-python-built-in-functions-packages-and-modules)
    - [2. **Keep It Simple, Stupid (KISS)**](#2-keep-it-simple-stupid-kiss)
    - [3. **Using Trigonometric, Logarithmic, and Exponential Functions from the Python Math Library**](#3-using-trigonometric-logarithmic-and-exponential-functions-from-the-python-math-library)
    - [4. **Comments in Python**](#4-comments-in-python)
    - [5. **Identifying and Fixing Common Errors Using Debugging Techniques**](#5-identifying-and-fixing-common-errors-using-debugging-techniques)
      - [Common Debugging Techniques:](#common-debugging-techniques)


### 1. **Python Built-In Functions, Packages, and Modules**

Python includes **built-in functions**, **modules**, and external **packages** that provide reusable functionality. Using them avoids rewriting solutions to common problems and keeps programs focused.

- **Built-in functions**: Python supplies these functions automatically, so they can be used without an import. Common examples include:
  - `print()`: Displays output to the user.
  - `len()`: Returns the length of an object (e.g., a string or list).
  - `int()`, `float()`, `str()`: Convert values between different data types.

Example:
```python
name = "Alice"
length = len(name)  # Using the built-in len() function to find the length of the string
print(length)  # Output: 5
```

- **Packages**: A package groups related modules and can be installed with Python’s package manager, `pip`, to add capabilities beyond the standard features.

Example:
```python
# To use the math package, you must first import it
import math

# Now you can access all the functions in the math module, like sqrt()
result = math.sqrt(16)  # Result is 4.0
```

- **Modules**: A module is a file containing reusable functions, classes, or variables. The `math` module, for example, supplies mathematical functions.

In general, a package can contain many modules, and each module can define several reusable functions.

### 2. **Keep It Simple, Stupid (KISS)**

The **KISS principle** emphasizes keeping solutions simple and straightforward. In programming, this means writing code that is easy to read, understand, and maintain. Avoid overcomplicating problems or adding unnecessary complexity.

Key takeaways:
- **Write simple code**: Focus on clarity and simplicity instead of trying to make the code overly efficient or complex.
- **Use existing tools**: Leverage built-in functions, packages, and modules rather than reinventing the wheel.

Example (KISS principle):
Instead of writing a complex loop to find the maximum value in a list, use Python's built-in `max()` function:
```python
numbers = [1, 2, 3, 4, 5]
max_value = max(numbers)  # Simple and efficient way to get the max value
print(max_value)  # Output: 5
```

### 3. **Using Trigonometric, Logarithmic, and Exponential Functions from the Python Math Library**

Python’s **math library** provides a wide range of mathematical functions, including trigonometric, logarithmic, and exponential operations. These functions help solve various problems in science and engineering.

Common functions in the `math` module:
- **Trigonometric Functions**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan2()`
- **Logarithmic Functions**: `log()`, `log10()`, `log2()`
- **Exponential Function**: `exp()`

Example of using the **math** module:
```python
import math

# Trigonometric example: sine of 30 degrees
angle_radians = math.radians(30)  # Convert degrees to radians
sine_value = math.sin(angle_radians)
print("Sine of 30 degrees:", sine_value)  # Output: 0.49999999999999994

# Logarithmic example: natural log of 10
log_value = math.log(10)
print("Log of 10:", log_value)  # Output: 2.302585092994046

# Exponential example: e raised to the power of 2
exp_value = math.exp(2)
print("Exponential of 2:", exp_value)  # Output: 7.3890560989306495
```

These functions are useful for scientific applications that involve angles, logarithms, or growth models (such as in physics, biology, and economics).

### 4. **Comments in Python**

**Comments** in Python are lines of text that are ignored by the interpreter. They are used to explain and document code, making it easier to understand for other developers (or your future self).

- **Single-line comments** are created by adding a `#` before the comment.
- **Multi-line comments** can be created using triple quotes (`'''` or `"""`), though these are generally used for docstrings (documentation strings).

Example of single-line and multi-line comments:
```python
# This is a single-line comment

# Function to calculate speed
def calculate_speed(distance, time):
    '''This function calculates speed based on distance and time.'''
    speed = distance / time  # Speed calculation
    return speed

# Call the function
print(calculate_speed(100, 20))  # Output: 5.0
```

Comments are essential for maintaining and understanding code, especially when the program becomes more complex.


