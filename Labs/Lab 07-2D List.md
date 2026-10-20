# Lab 7–2D List

### Question(s)

1. Average Each Row:
   
   - Write a function `calc_row_avg(numss)` that calculates the average for every row of a 2D list
   
#### Example:
```python
def calc_row_avg(numss):
   # code

calc_row_avg([[1,2,3],[4,5,6],[7,8,9]]) # returns [2.0, 5.0, 8.0]
```

2. Average Each Column:
   - Write a function `calc_col_avg(numss)` that calculates the average for every column of a 2D list
   
   #### Example:
```python
def calc_col_avg(numss):
    # code

calc_col_avg([[1,2,3],[4,5,6],[7,8,9]]) # returns [4, 5, 6]
```

3. Magic Square Validation:
   
   - Write a function `is_magic_square(matrix)` that checks if a given **N x N** matrix is a magic square.
   
   #### Example:
```python
def is_magic_square(numss): 
   # code

is_magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]])  # Returns True
is_magic_square([[4, 9, 2], [8, 1, 6], [3, 5, 7]])  # Returns False
```
   ✅ **Hints:** Verify that all rows, columns, and both diagonals sum to the same value.
