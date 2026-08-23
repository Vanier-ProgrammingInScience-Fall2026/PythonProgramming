# Lecture 1: Intro to Programming

### **Table of Contents**

- [Lecture 1: Intro to Programming](#lecture-1-intro-to-programming)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Introduction to Programming in Python**](#1-introduction-to-programming-in-python)
    - [2. **Statements and Expressions**](#2-statements-and-expressions)
      - [**What is a Statement?**](#what-is-a-statement)
      - [**What is an Expression?**](#what-is-an-expression)
    - [3. **Variables and Assignments**](#3-variables-and-assignments)
      - [**Naming Conventions**](#naming-conventions)
    - [4. **Working with Data Types**](#4-working-with-data-types)
    - [5. **Input and Output Statements**](#5-input-and-output-statements)
      - [**Input**](#input)
      - [**Output**](#output)
    - [6. **Fundamental Programming Principles**](#6-fundamental-programming-principles)
      - [**Naming Conventions (Principles)**](#naming-conventions-principles)
      - [**Keep It Simple, Stupid (KISS)**](#keep-it-simple-stupid-kiss)
      - [**Open/Closed Principle**](#openclosed-principle)
      - [**Don't Repeat Yourself (DRY)**](#dont-repeat-yourself-dry)
      - [**Early Testing and Debugging**](#early-testing-and-debugging)

### 1. **Introduction to Programming in Python**

A **programming language** such as Python gives people a precise way to describe solutions for a computer. A program combines valid syntax with logical instructions that the computer can interpret and run. Python is especially popular in scientific work because it is readable, flexible, and supported by a large ecosystem of tools.

### 2. **Statements and Expressions**

#### **What is a Statement?**
In programming, a **statement** is an instruction that carries out an action. Python statements include assignments, function calls, loops, and conditional blocks.

Example:
```python
x = 10  # Assignment statement
print(x)  # Function call statement
```

Each statement tells Python to do something, such as store a value or call a function.

#### **What is an Expression?**
An **expression** combines values, variables, and operators and evaluates to a result. That result can then be used as part of another statement.

Example:
```python
y = x + 5  # x + 5 is an expression that evaluates to 15 if x is 10
```

### 3. **Variables and Assignments**

A **variable** is a name that refers to a value while a program runs. **Assignment** gives that name an initial value or replaces its current value.

Example:
```python
temperature = 25  # Assigning a value to a variable
```

#### **Naming Conventions**
In Python, good naming conventions are important for maintaining clear and readable code. Some best practices for naming variables and functions include:
- **Use descriptive names**: e.g., `temperature`, `distance`, `calculate_speed`.
- **Use snake_case** for variables and functions: e.g., `calculate_speed`.
- **Avoid reserved keywords**: such as `if`, `for`, `while`, etc.
- **Start with a letter**: Variables should start with a letter, not a number.

### 4. **Working with Data Types**

Python has several built-in data types, which are essential for working with different kinds of data. Some common types include:
- **int**: Integer numbers, e.g., `5`, `100`.
- **float**: Floating-point numbers, e.g., `3.14`, `-0.001`.
- **str**: String (text) data, e.g., `"Hello, world!"`.
- **bool**: Boolean values (`True` or `False`).
- **list**: A collection of items, e.g., `[1, 2, 3]`.
- **tuple**: An immutable collection of items, e.g., `(1, 2, 3)`.

Python uses **dynamic typing**, so a variable’s type is inferred from the value assigned to it rather than declared separately.

Example:
```python
age = 30  # Integer
name = "Alice"  # String
height = 1.75  # Float
```

Python allows a variable to refer to values of different types at different times, but keeping a consistent type usually makes code easier to understand.

Example:
```python
# not suggested
x = 5    # Integer
x = "hello"    # String
x = True    # Boolean
```

### 5. **Input and Output Statements**

**Input** brings data into a program, while **output** communicates information back to the user.

#### **Input**
In Python, input can be taken using the `input()` function, which returns a `string`. You can then convert it to other data types as needed.

Example:
```python
name = input("Enter your name: ")  # Input
age = int(input("Enter your age: "))  # Input and conversion to int
```

#### **Output**
Output is displayed using the `print()` function.

Example:
```python
print("Hello, " + name)  # Output
print("Your age is " + str(age))  # Output (converted to string)
```

### 6. **Fundamental Programming Principles**

These principles help to write better, cleaner, and more maintainable code.

#### **Naming Conventions (Principles)**
Following consistent and meaningful naming conventions for variables and functions makes code easier to read and maintain. Use **descriptive names** and follow **snake_case** style in Python.

#### **Keep It Simple, Stupid (KISS)**
The KISS principle emphasizes that solutions should be simple. Avoid overcomplicating code. In Python, you can use built-in functions and libraries to simplify your tasks.

Key takeaway: **Write clear, simple, and easy-to-understand code.**

#### **Open/Closed Principle**
The Open/Closed Principle suggests that software entities (such as classes or functions) should be **open for extension**, but **closed for modification**. This is especially useful in object-oriented programming when building more flexible and reusable code.

Key takeaway: **Extend, don’t modify**.

#### **Don't Repeat Yourself (DRY)**
Avoid repeating code. If you find yourself writing similar code multiple times, refactor it into a reusable function or method. Python's functions and modules can help you implement this principle effectively.

Key takeaway: **Write reusable code and reduce redundancy.**

#### **Early Testing and Debugging**
Testing and debugging are essential in programming. Start testing your code early in the development process to ensure it works as expected. Python provides built-in tools like `assert` and the `unittest` module for automated testing.

Key takeaway: **Test early and often to catch errors quickly.**
