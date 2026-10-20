# Lecture 8: 2D Arrays and Slicing

### **Table of Contents**

1. [Introduction to Two-Dimensional Arrays](#introduction-to-two-dimensional-arrays)
2. [Creating and Accessing Two-Dimensional Arrays](#creating-and-accessing-two-dimensional-arrays)
3. [Slicing in Two-Dimensional Arrays](#slicing-in-two-dimensional-arrays)
4. [Debugging and Testing Two-Dimensional Arrays and Slicing](#debugging-and-testing-two-dimensional-arrays-and-slicing)

### 1. **Introduction to Two-Dimensional Arrays**

A **two-dimensional array** stores values in a grid of rows and columns. In basic Python, it is commonly represented as a **list of lists**. Accessing an element requires one index for its row and another for its column.

For example, a 2D array with 3 rows and 4 columns can be visualized as follows:

```
[ [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12] ]
```

This example contains three rows, with four elements in each row.

### 2. **Creating and Accessing Two-Dimensional Arrays**

Create a **two-dimensional array** by placing one list inside another. Each inner list represents a row.

#### Example of Creating a 2D Array:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

You can access elements of a 2D array by using two indices: one for the row and one for the column.

#### Accessing an Element:
```python
# Access element in the first row, second column (indexing starts at 0)
element = matrix[0][1]
print(element)  # Output: 2
```

In the example above:
- `matrix[0]` refers to the first row (`[1, 2, 3]`).
- `matrix[0][1]` refers to the second element in the first row, which is `2`.

#### Modifying an Element:
You can modify an element in a two-dimensional array by accessing its position using row and column indices:
```python
# Modify the element in the second row, third column
matrix[1][2] = 10
print(matrix[1])  # Output: [4, 5, 10]
```

### 3. **Slicing in Two-Dimensional Arrays**

**Slicing** allows you to access a subset of elements from a list or array. In the case of two-dimensional arrays, slicing enables you to extract rows, columns, or sub-arrays (a block of rows and columns).

#### Slicing Rows:
You can slice a two-dimensional array to access specific rows. For example, to get the first two rows of a matrix:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Slice to get the first two rows
sub_matrix = matrix[:2]
print(sub_matrix)  # Output: [[1, 2, 3], [4, 5, 6]]
```

Here, `matrix[:2]` slices the matrix from the start up to (but not including) the second index, giving us the first two rows.

#### Slicing Columns:
To slice columns, you can iterate over each row and slice the desired columns.
```python
# Get the first column from each row
first_column = [row[0] for row in matrix]
print(first_column)  # Output: [1, 4, 7]
```

Here, a **list comprehension** is used to extract the first element (column) of each row.

#### Slicing a Sub-Array (Sub-Matrix):
You can also slice a sub-array (a specific range of rows and columns). For example, to get the first two rows and the first two columns:
```python
sub_array = [row[:2] for row in matrix[:2]]
print(sub_array)  # Output: [[1, 2], [4, 5]]
```

Here:
- `matrix[:2]` slices the first two rows.
- `row[:2]` slices the first two elements (columns) from each of the selected rows.

### 4. **Debugging and Testing Two-Dimensional Arrays and Slicing**

When working with two-dimensional arrays and slicing, it’s essential to test your code to ensure you're accessing and modifying the array correctly.

#### Debugging with Print Statements:
Use **print statements** to verify the content of the array or sub-array during slicing. This will help ensure that you’re extracting the correct rows and columns.

Example:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Debugging: Print the full matrix and sub-array
print("Full matrix:", matrix)
sub_matrix = matrix[:2]
print("Sub-matrix (first two rows):", sub_matrix)
```

#### Testing Edge Cases:
- **Empty arrays**: Check how your code handles cases where the array is empty or contains no rows.
- **Slicing beyond bounds**: Test how your code behaves when you slice beyond the available number of rows or columns.

Example of an edge case (empty matrix):
```python
empty_matrix = []

# Slicing an empty matrix should return an empty list
print(empty_matrix[:2])  # Output: []
```

#### Testing Slicing on Non-Square Matrices:
Make sure to test slicing with matrices where the number of rows and columns is not equal, such as a **rectangular array**.

Example:
```python
rectangular_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Slice first two rows and first three columns
print([row[:3] for row in rectangular_matrix])  # Output: [[1, 2, 3], [5, 6, 7]]
```
