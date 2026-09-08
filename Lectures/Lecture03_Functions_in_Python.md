# Lecture 3: Functions in Python

## Table of Contents

- [1. Introduction to Functions](#1-introduction-to-functions)
- [2. Built-In Functions](#2-built-in-functions)
- [3. Using Functions from Modules](#3-using-functions-from-modules)
- [4. Useful Functions from the Math Module](#4-useful-functions-from-the-math-module)
- [5. Keep It Simple, Stupid (KISS)](#5-keep-it-simple-stupid-kiss)
- [6. User-Defined Functions](#6-user-defined-functions)
- [7. Parameters and Arguments](#7-parameters-and-arguments)
- [8. Returning Values from Functions](#8-returning-values-from-functions)
- [9. Calling a Function](#9-calling-a-function)
- [10. Naming Functions](#10-naming-functions)
- [11. Why Do We Use Functions?](#11-why-do-we-use-functions)
- [12. Single Responsibility](#12-single-responsibility)
- [13. Refactoring Code Using Functions](#13-refactoring-code-using-functions)
- [14. Comments in Python](#14-comments-in-python)

---

## 1. Introduction to Functions

A **function** is a reusable block of code that performs a specific task.

We have already used several functions in Python, even if we did not call them functions at the time.

For example:

```python
print("Hello")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

Here:

- `print()` is a function.
- `input()` is a function.
- `int()` is a function.

Functions help us avoid writing everything from scratch.

There are two main types of functions that we will use:

1. **Existing functions** provided by Python or its modules.
2. **User-defined functions** that we create ourselves.

---

# Part 1 — Existing Functions

## 2. Built-In Functions

Python provides many **built-in functions**.

Built-in functions are available automatically. We do **not** need to import anything before using them.

Some common built-in functions include:

- `print()` — displays output.
- `input()` — gets input from the user.
- `int()` — converts a value to an integer.
- `float()` — converts a value to a floating-point number.
- `str()` — converts a value to a string.
- `len()` — returns the length of a string or another object.
- `max()` — returns the largest value.
- `min()` — returns the smallest value.
- `round()` — rounds a number.

### Example: `len()`

```python
name = "Alice"

length = len(name)

print(length)
```

Output:

```text
5
```

The function:

```python
len(name)
```

returns the number of characters in `"Alice"`.

### Example: `max()`

```python
x1 = 4
x2 = 9

larger_x = max(x1, x2)

print(larger_x)
```

Output:

```text
9
```

Instead of writing our own code to determine which value is larger, we can simply use `max()`.

### Example: `round()`

```python
distance = 10.45678

rounded_distance = round(distance, 2)

print(rounded_distance)
```

Output:

```text
10.46
```

The second argument tells Python how many decimal places we want.

```python
round(distance, 2)
```

means:

> Round `distance` to **2 decimal places**.

---

## 3. Using Functions from Modules

Python also provides **modules**.

A **module** is a file containing useful functions, variables, and other Python code that we can reuse.

Unlike built-in functions, functions inside a module usually need to be imported before we can use them.

One important module for science and mathematics is the `math` module.

To use it:

```python
import math
```

After importing it, we can access functions from the module using:

```python
math.function_name()
```

For example:

```python
import math

result = math.sqrt(16)

print(result)
```

Output:

```text
4.0
```

Here:

```python
math.sqrt(16)
```

uses the `sqrt()` function from the `math` module.

### Built-In Function vs. Module Function

Compare:

```python
round(5.678, 2)
```

with:

```python
math.sqrt(16)
```

`round()` is a **built-in function**, so no import is required.

`sqrt()` belongs to the **math module**, so we first need:

```python
import math
```

---

## 4. Useful Functions from the Math Module

The `math` module contains many useful mathematical functions.

First, import it:

```python
import math
```

### Square Root

```python
result = math.sqrt(25)

print(result)
```

Output:

```text
5.0
```

### Powers

Python can calculate powers directly using `**`:

```python
result = 5 ** 2

print(result)
```

Output:

```text
25
```

The `math` module also contains:

```python
math.pow(5, 2)
```

### Trigonometric Functions

Some useful trigonometric functions include:

```python
math.sin()
math.cos()
math.tan()
```

Python's trigonometric functions use **radians**, not degrees.

We can convert degrees to radians using:

```python
math.radians()
```

Example:

```python
import math

angle = 30
angle_radians = math.radians(angle)

sine_value = math.sin(angle_radians)

print(sine_value)
```

The result is approximately:

```text
0.5
```

### Converting Radians to Degrees

We can also convert radians back to degrees:

```python
math.degrees()
```

Example:

```python
import math

angle_radians = math.pi / 2

angle_degrees = math.degrees(angle_radians)

print(angle_degrees)
```

Output:

```text
90.0
```

### `atan2()`

The function:

```python
math.atan2(y, x)
```

can be used to calculate an angle from two components.

For example:

```python
import math

force_x = 3
force_y = 4

angle_radians = math.atan2(force_y, force_x)
angle_degrees = math.degrees(angle_radians)

print(angle_degrees)
```

### Logarithmic Functions

The `math` module also contains logarithmic functions:

```python
math.log()
math.log10()
math.log2()
```

Example:

```python
import math

result = math.log10(100)

print(result)
```

Output:

```text
2.0
```

### Exponential Function

The exponential function is:

```python
math.exp()
```

For example:

```python
import math

result = math.exp(2)

print(result)
```

This calculates:

```text
e²
```

---

## 5. Keep It Simple, Stupid (KISS)

The **KISS principle** means:

> Keep your solution simple and easy to understand.

In programming, we should avoid making a solution more complicated than necessary.

Whenever Python already provides a function that performs the task, we should usually use it instead of rewriting the same functionality ourselves.

For example:

```python
x1 = 5
x2 = 8

larger_x = max(x1, x2)

print(larger_x)
```

Output:

```text
8
```

Using existing functions makes programs:

- shorter,
- easier to read,
- easier to understand,
- easier to maintain.

---

# Part 2 — User-Defined Functions

## 6. User-Defined Functions

Python gives us many useful existing functions.

However, sometimes we need a function for a task that is specific to our own program.

Python allows us to create our own functions.

These are called **user-defined functions**.

A user-defined function is a named block of code that performs a particular task.

The basic syntax is:

```python
def function_name(parameters):
    # Code to execute
    return result
```

For example:

```python
def greet(name):
    return "Hello, " + name + "!"
```

The keyword:

```python
def
```

means **define a function**.

The name of this function is:

```python
greet
```

The function receives one value:

```python
name
```

and returns a result.

---

## 7. Parameters and Arguments

Consider this function:

```python
def greet(name):
    return "Hello, " + name + "!"
```

The variable:

```python
name
```

is called a **parameter**.

A parameter is a variable that receives a value when the function is called.

For example:

```python
greet("Alice")
```

Here:

```text
"Alice"
```

is called an **argument**.

So:

```python
def greet(name):
```

`name` is the **parameter**.

And:

```python
greet("Alice")
```

`"Alice"` is the **argument**.

### More Than One Parameter

A function can receive several parameters.

Example:

```python
def calculate_speed(distance, time):
    speed = distance / time
    return speed
```

This function has two parameters:

```text
distance
time
```

We can call it using:

```python
calculate_speed(100, 20)
```

Here:

```text
100
```

is passed to `distance`, and:

```text
20
```

is passed to `time`.

---

## 8. Returning Values from Functions

A function can calculate a value and send that value back to the part of the program that called it.

We use:

```python
return
```

for this purpose.

Example:

```python
def calculate_speed(distance, time):
    speed = distance / time
    return speed
```

When we call:

```python
calculate_speed(100, 20)
```

the function calculates:

```text
100 / 20
```

and returns:

```text
5.0
```

We can store the returned value in a variable:

```python
speed = calculate_speed(100, 20)

print(speed)
```

Output:

```text
5.0
```

### Returning an Expression Directly

We do not always need to create a variable inside the function.

Instead of:

```python
def calculate_speed(distance, time):
    speed = distance / time
    return speed
```

we can write:

```python
def calculate_speed(distance, time):
    return distance / time
```

Both versions return the same result.

For beginners, either form is acceptable. The first version can sometimes make the calculation easier to follow.

---

## 9. Calling a Function

Defining a function does **not** automatically execute it.

For example:

```python
def greet(name):
    return "Hello, " + name + "!"
```

Python now knows that the function exists, but nothing is displayed yet.

We must **call the function**:

```python
message = greet("Alice")

print(message)
```

Output:

```text
Hello, Alice!
```

We can also write:

```python
print(greet("Alice"))
```

Output:

```text
Hello, Alice!
```

The process is:

```text
Define the function
        ↓
Call the function
        ↓
Pass arguments
        ↓
Function performs its task
        ↓
Function returns a result
```

### Example

```python
def calculate_distance(speed, time):
    distance = speed * time
    return distance


distance = calculate_distance(20, 5)

print("Distance:", distance)
```

Output:

```text
Distance: 100
```

---

## 10. Naming Functions

Good function names make programs easier to understand.

Function names should describe what the function does.

### Use Descriptive Names

Good:

```python
calculate_speed()
```

Less clear:

```python
calc()
```

Bad:

```python
function1()
```

### Use `snake_case`

Python function names normally use **snake_case**.

This means:

- lowercase letters,
- words separated using underscores.

Good:

```python
calculate_speed()
calculate_distance()
convert_temperature()
```

Avoid:

```python
CalculateSpeed()
calculateSpeed()
```

### Function Names Usually Describe an Action

Functions usually **do something**, so names often begin with verbs such as:

```text
calculate
convert
find
display
get
```

Examples:

```python
calculate_speed()
convert_temperature()
find_distance()
```

---

## 11. Why Do We Use Functions?

Functions are useful because they help us organize and reuse code.

### Organize Our Code

Instead of writing one long program, we can divide it into smaller tasks.

For example:

```python
def calculate_velocity(distance, time):
    return distance / time


def calculate_distance(velocity, time):
    return velocity * time


def calculate_time(distance, velocity):
    return distance / velocity
```

Each function performs one specific calculation.

### Reuse Code

Once a function has been defined, we can call it several times.

```python
def calculate_distance(speed, time):
    return speed * time


distance1 = calculate_distance(20, 5)
distance2 = calculate_distance(10, 8)
distance3 = calculate_distance(25, 3)

print(distance1)
print(distance2)
print(distance3)
```

We do not need to rewrite the calculation each time.

### Make Programs Easier to Understand

Compare:

```python
result = 120 / 3
```

with:

```python
result = calculate_speed(120, 3)
```

The function name tells us what the calculation represents.

### Make Programs Easier to Change

If a calculation is used several times, putting it inside a function means we have one clear place where that calculation is defined.

---

## 12. Single Responsibility

A useful rule when creating functions is:

> A function should perform one clear task.

This is called the **Single Responsibility Principle**.

For example:

```python
def calculate_speed(distance, time):
    return distance / time
```

This function has one responsibility:

> Calculate speed.

Keeping functions focused makes programs easier to:

- understand,
- test,
- debug,
- reuse.

### Calculation and Output

In many cases, it is useful to separate a calculation from displaying its result.

For example:

```python
def calculate_speed(distance, time):
    return distance / time


speed = calculate_speed(100, 20)

print("Speed:", speed)
```

The function performs the calculation, while the main program handles the output.

This makes the function reusable in other parts of the program.

---

## 13. Refactoring Code Using Functions

**Refactoring** means reorganizing existing code to make it clearer or easier to reuse without changing what the program does.

Suppose we originally write:

```python
distance1 = 20 * 5
distance2 = 20 * 8
distance3 = 20 * 10

print(distance1)
print(distance2)
print(distance3)
```

We notice that the same calculation appears several times.

We can move that calculation into a function:

```python
def calculate_distance(speed, time):
    return speed * time


distance1 = calculate_distance(20, 5)
distance2 = calculate_distance(20, 8)
distance3 = calculate_distance(20, 10)

print(distance1)
print(distance2)
print(distance3)
```

The program performs the same calculations, but the repeated logic is now organized inside a reusable function.

This is an example of **refactoring**.

---

## 14. Comments in Python

Comments are notes inside our code that Python ignores.

They help explain the purpose of the code.

A single-line comment starts with:

```python
#
```

Example:

```python
# Calculate the speed of an object
speed = distance / time
```

Comments can also be placed beside code:

```python
speed = distance / time  # Calculate speed
```

### Comments Inside Functions

Comments can help explain what a function is doing.

```python
def calculate_speed(distance, time):
    # Calculate and return the speed
    speed = distance / time
    return speed
```

However, comments should explain something useful.

Avoid unnecessary comments such as:

```python
x = 5  # Set x equal to 5
```

The code is already clear enough.

Good variable and function names often reduce the need for many comments.
