# Lecture 7: Lists and Arrays


### **Table of Contents**

1. [Introduction to Lists and Single Dimensional Arrays](#introduction-to-lists-and-single-dimensional-arrays)
2. [Don't Repeat Yourself (DRY) Principle](#dont-repeat-yourself-dry-principle)
3. [Arithmetic Operations with Arrays](#arithmetic-operations-with-arrays)
4. [Debugging and Testing Array Operations](#debugging-and-testing-array-operations)

### 1. **Introduction to Lists and Single Dimensional Arrays**

In Python, **lists** are the standard way to store an ordered collection of items. A list can contain numbers, strings, or other lists; it is **mutable** and may contain duplicate values.

Although a **Python list** is not identical to an array in languages such as C++ or Java, both structures store multiple elements that can be accessed by index.

A **single-dimensional array** is essentially a list where all elements are arranged in a single line or sequence.

#### Basic List Syntax:
```python
my_list = [10, 20, 30, 40, 50]  # A list of integers
```

#### Accessing Elements in a List:
You can access elements in a list using **indexing**:
```python
first_element = my_list[0]  # Accesses the first element, 10
last_element = my_list[-1]  # Accesses the last element, 50
```

You can also use **slicing** to access a subset of a list:
```python
subset = my_list[1:4]  # Accesses elements from index 1 to 3, i.e., [20, 30, 40]
```

### 2. **Don't Repeat Yourself (DRY) Principle**

The **Don't Repeat Yourself (DRY)** principle recommends keeping each piece of logic in one place. Repeated code is harder to update and creates more opportunities for inconsistent fixes. **Functions** and **loops** are common ways to centralize repeated work.

#### DRY in Lists:
In Python, using loops and functions can help avoid repetition. For example, instead of manually summing elements of a list multiple times, you can create a function that performs this operation.

Example:
```python
# Repetitive code without DRY
sum1 = 10 + 20 + 30
sum2 = 40 + 50 + 60

# DRY approach using a function
def calculate_sum(numbers):
    return sum(numbers)

numbers1 = [10, 20, 30]
numbers2 = [40, 50, 60]
print(calculate_sum(numbers1))  # Output: 60
print(calculate_sum(numbers2))  # Output: 150
```

By using the DRY principle, the calculation logic is now reusable and easier to maintain.

### 3. **Arithmetic Operations with Arrays**

Arrays (or lists) allow you to perform arithmetic operations on their elements. You can use Python’s built-in operators, or you can use the **NumPy** library for more advanced array operations. However, we will start with basic arithmetic operations using lists without external libraries.

#### Basic Arithmetic Operations on Lists:
You can perform arithmetic operations like addition, subtraction, multiplication, and division on the elements of a list using a **for loop** or **list comprehension**.

Example of addition (adding the same number to each element of the list):
```python
numbers = [10, 20, 30, 40]

# Adding 5 to each element
new_numbers = [num + 5 for num in numbers]
print(new_numbers)  # Output: [15, 25, 35, 45]
```

#### Example of multiplication (multiplying each element by 2):
```python
numbers = [1, 2, 3, 4]

# Multiplying each element by 2
multiplied_numbers = [num * 2 for num in numbers]
print(multiplied_numbers)  # Output: [2, 4, 6, 8]
```

#### Summing All Elements:
To calculate the sum of all elements in a list, you can use Python’s built-in `sum()` function:
```python
numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)  # Output: 100
```

#### Performing Element-wise Arithmetic Operations:
You can perform element-wise operations on two lists using a **for loop** or **list comprehension**. For example, if you want to add corresponding elements of two lists:

```python
list1 = [10, 20, 30]
list2 = [1, 2, 3]

# Adding corresponding elements
sum_lists = [a + b for a, b in zip(list1, list2)]
print(sum_lists)  # Output: [11, 22, 33]
```

The `zip()` function pairs up corresponding elements from two lists, allowing you to perform the operation on them in parallel.

### 4. **Debugging and Testing Array Operations**

When working with lists and arrays, it's important to ensure that the operations are being performed correctly. Here are some debugging techniques for working with arrays:

#### Print Statements
Use **print statements** to check the values of the array before and after operations:
```python
numbers = [10, 20, 30]

# Debugging: Check the array before performing arithmetic
print("Original numbers:", numbers)

# Perform an operation
updated_numbers = [num + 5 for num in numbers]

# Debugging: Check the updated array
print("Updated numbers:", updated_numbers)
```

#### Testing Edge Cases
Test the behavior of the array operations with edge cases:
- **Empty lists**: Check if your code handles empty arrays gracefully.
- **Large numbers**: Ensure the operations work correctly with large numbers.
- **Negative numbers**: Check how your code handles negative values.

Example with an empty list:
```python
numbers = []

# Avoid errors when performing operations on an empty list
if numbers:
    updated_numbers = [num + 5 for num in numbers]
    print("Updated numbers:", updated_numbers)
else:
    print("The list is empty!")
```
