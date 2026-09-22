# Lecture 6: Iterative Logic

### **Table of Contents**

- [Lecture 6: Iterative Logic](#lecture-6-iterative-logic)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Introduction to Iterative Logic**](#1-introduction-to-iterative-logic)
    - [2. **The `for` Loop**](#2-the-for-loop)
      - [Syntax:](#syntax)
    - [3. **The `while` Loop**](#3-the-while-loop)
      - [Syntax:](#syntax-1)
    - [4. **`break` and `continue` Statements**](#4-break-and-continue-statements)
      - [The `break` Statement](#the-break-statement)
      - [The `continue` Statement](#the-continue-statement)
    - [5. **Debugging and Testing Iterative Logic**](#5-debugging-and-testing-iterative-logic)
      - [Debugging with Print Statements](#debugging-with-print-statements)
      - [Testing Loops for Edge Cases](#testing-loops-for-edge-cases)

### 1. **Introduction to Iterative Logic**

Use **iterative logic** when a task must be repeated. **Loops** run a block of code for a sequence of values or while a condition remains `True`.

There are two main types of loops in Python:
- The **`for` loop**: Used when you know in advance how many times you want to repeat a block of code.
- The **`while` loop**: Used when you want to repeat a block of code as long as a condition is true, but you may not know how many iterations will be needed.

Both loop types handle repetition efficiently, and `break` and `continue` provide additional control over the loop’s progress.

### 2. **The `for` Loop**

The **`for` loop** visits each item in a sequence, such as a **list**, **tuple**, or **string**, or in a range of numbers. It is a good choice when the values to process are known in advance.

#### Syntax:
```python
for variable in sequence:
    # Code to execute for each item in the sequence
```

The **variable** takes the value of each item in the **sequence** for each iteration.

Example:
```python
# Iterating through a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

This will print:
```
1
2
3
4
5
```

The `range()` function is commonly used with **`for` loops** to generate a sequence of numbers:
```python
for i in range(5):  # Will iterate over numbers 0 to 4
    print(i)
```

This will print:
```
0
1
2
3
4
```

### 3. **The `while` Loop**

The **`while` loop** is used when you want to repeat a block of code as long as a certain condition is `True`. It is useful when you do not know in advance how many times the loop should run.

#### Syntax:
```python
while condition:
    # Code to execute as long as the condition is true
```

The loop continues to run until the **condition** becomes `False`.

Example:
```python
# Print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment the counter to avoid infinite loop
```

This will print:
```
1
2
3
4
5
```

### 4. **`break` and `continue` Statements**

`break` and `continue` are special statements used to control the flow of loops.

#### The `break` Statement

The `break` statement is used to exit the loop prematurely, even if the loop condition is still `True`. It is often used when you want to stop the loop based on a specific condition.

Example:
```python
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is equal to 5
    print(i)
```

This will print:
```
0
1
2
3
4
```
The loop stops when `num` reaches 5, and the remaining numbers are not printed.

#### The `continue` Statement

The `continue` statement skips the current iteration of the loop and moves to the next iteration. It is used when you want to skip certain steps within the loop without exiting the entire loop.

Example:
```python
for num in range(10):
    if num == 5:
        continue  # Skip this iteration when num is equal to 5
    print(num)
```

This will print:
```
0
1
2
3
4
6
7
8
9
```

The number `5` is skipped because the loop continues to the next iteration when `num` is 5.

### 5. **Debugging and Testing Iterative Logic**

When working with loops, it is essential to test and debug to avoid issues like **infinite loops** (when the loop never ends) or **off-by-one errors** (when the loop does not iterate the expected number of times).

#### Debugging with Print Statements
- Use **`print` statements** to check if the loop is running as expected, especially to track variable values.
- Ensure that the loop condition is changing as intended to avoid infinite loops.

Example:
```python
count = 1
while count <= 5:
    print("Current count:", count)  # Debugging: Check the value of count
    count += 1
```

#### Testing Loops for Edge Cases
- Test loops with different ranges or boundary conditions to ensure they handle all situations, such as empty lists or starting from different values.

Example of testing a **`for` loop** with an empty list:
```python
numbers = []
for number in numbers:
    print(number)  # This will not print anything because the list is empty
```

Example of testing a **`while` loop** with boundary conditions:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

By using debugging techniques, such as checking variable values and testing edge cases, you can ensure that your loops behave as expected and perform the correct number of iterations.
