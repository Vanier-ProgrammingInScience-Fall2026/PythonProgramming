# Lecture 4: User-Defined Functions

### **Table of Contents**

- [Lecture 4: User-Defined Functions](#lecture-4-user-defined-functions)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Introduction to User-Defined Functions**](#1-introduction-to-user-defined-functions)
      - [Syntax:](#syntax)
    - [2. **Naming Conventions for Functions**](#2-naming-conventions-for-functions)
    - [3. **Keep It Simple, Stupid (KISS) and Single Responsibility**](#3-keep-it-simple-stupid-kiss-and-single-responsibility)
      - [**Single Responsibility**:](#single-responsibility)
    - [4. **Open/Closed Principle in Functions**](#4-openclosed-principle-in-functions)
    - [5. **Enhance Code Structure and Logic Through Functions**](#5-enhance-code-structure-and-logic-through-functions)
    - [6. **Refactoring Code**](#6-refactoring-code)

### 1. **Introduction to User-Defined Functions**

A **user-defined function** is a named block of Python code that performs a focused task. Functions divide complex problems into smaller pieces, reduce repetition, and let the same logic be called with different inputs.

#### Syntax:
```python
def function_name(parameters):
    # Code block to execute
    return result
```

- **`def`**: Keyword used to define a function.
- **`function_name`**: Name of the function (following Python's naming conventions).
- **`parameters`**: Input values passed to the function (optional).
- **`return`**: Returns a value from the function (optional).

Example:
```python
def greet(name):
    return "Hello, " + name + "!"
    
print(greet("Alice"))
```

This will output:
```
Hello, Alice!
```

### 2. **Naming Conventions for Functions**

Consistent names make code easier to read and maintain. A function name should tell the reader what the function does; common Python conventions include:

- **Use descriptive names**: The function name should clearly describe what the function does. For example, use `calculate_area()` instead of `calc()`.
- **Use snake_case**: In Python, function names should be written in **snake_case**, meaning all letters are lowercase, and words are separated by underscores. For example, `calculate_speed()` is preferred over `CalculateSpeed()`.
- **Avoid overly generic names**: Avoid using names like `do_stuff()` or `function1()` that don't describe the function's behavior.

Good example:
```python
def calculate_area(radius):
    return 3.14 * radius ** 2
```

### 3. **Keep It Simple, Stupid (KISS) and Single Responsibility**

The **KISS principle** suggests that functions should be simple and easy to understand. Overcomplicating a function can lead to bugs and maintenance challenges. Functions should do one thing and do it well.

#### **Single Responsibility**:
Each function should have a **single responsibility**, meaning it should only perform one specific task. A function that tries to do too many things can become difficult to understand and debug.

Example:
- **Bad**: A function that calculates the area and prints a message.
```python
def area_and_message(radius):
    area = 3.14 * radius ** 2
    print("The area is:", area)
    return area
```

- **Good**: Two separate functions, each with a single responsibility.
```python
def calculate_area(radius):
    return 3.14 * radius ** 2

def print_area(area):
    print("The area is:", area)
```

### 4. **Open/Closed Principle in Functions**

The **Open/Closed Principle** suggests that software entities (like functions) should be **open for extension**, but **closed for modification**. This means you should be able to add new functionality to a function without changing its original code.

In Python, you can achieve this principle by writing functions that can easily be extended with new functionality.

Example:
```python
# Original function that calculates area of a circle
def calculate_area(radius):
    return 3.14 * radius ** 2

# Extended function that also calculates the circumference without modifying the original function
def calculate_circumference(radius):
    return 2 * 3.14 * radius
```

Here, you’ve extended the functionality by adding `calculate_circumference()` without modifying the original `calculate_area()` function, which adheres to the Open/Closed Principle.

### 5. **Enhance Code Structure and Logic Through Functions**

One of the key benefits of functions is that they allow you to structure your code more logically. You can break down large problems into smaller, more manageable tasks by using functions to represent different parts of your logic.

For example, if you are solving a physics problem involving the calculation of velocity, distance, and time, you could break the problem down into separate functions:
```python
def calculate_velocity(distance, time):
    return distance / time

def calculate_distance(velocity, time):
    return velocity * time

def calculate_time(distance, velocity):
    return distance / velocity
```

Now, instead of writing a long and complex series of calculations, you can reuse these smaller functions throughout your code to keep everything organized.

### 6. **Refactoring Code**

**Refactoring** refers to the process of restructuring existing code without changing its external behavior. It improves the readability, maintainability, and efficiency of code. You might refactor code to eliminate duplication, improve naming conventions, or simplify complex logic.

Common reasons to refactor code:
- **Simplify complex functions**: If a function is doing too much, break it into smaller, more manageable pieces.
- **Improve readability**: Make the code more understandable to other developers (or your future self).
- **Eliminate redundant code**: If the same logic is repeated, refactor it into a function or loop.

Example of refactoring:
```python
# Original code
def total_cost(price1, price2, price3):
    return price1 + price2 + price3

# Refactored code with a loop
def total_cost(prices):
    total = 0
    for price in prices:
        total += price
    return total
```

The refactored version is more scalable because it can handle any number of prices without modifying the function.
