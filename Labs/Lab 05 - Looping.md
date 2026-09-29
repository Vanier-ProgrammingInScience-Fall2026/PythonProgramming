# Programming in Science – Lab 5-Loop01

### Question(s) 

1. Write a function `draw_hollow_square(n)` that returns a string representing a hollow square pattern of stars (`*`) with side length `n`.

#### Example (n = 5):
```
*****
*   *
*   *
*   *
*****
```
✅ **Hints:** Use a `for` loop or a `while` loop and construct each line, appending them to a result string.

2. Write a function `print_number_pattern(n)` that returns a string representing a number pattern of height `n` **without using a `for` loop inside the print statement**.

#### Example (n = 4):
```
1
12
123
1234
```
✅ **Hints:** Use nested `for` loops or `while` loops to build the pattern.

3. Write a function `sum_of_natural_numbers(n)` that **returns the sum** of the first `n` natural numbers using a `for` loop or a `while` loop. The output must follow the pattern displayed in the example below.

#### Example:
For `n = 5`:
```
Sum = 1 + 2 + 3 + 4 + 5 = 15
```
✅ **Hints:** Use a counter-variable and accumulate the total.

4. Write a function `print_centered_star_pyramid(n)` that returns a string representing a centered pyramid of stars (`*`) with height `n`.

#### Example (n = 4):
```
   *
  ***
 *****
*******
```
✅ **Hints:** Use spaces before stars to center the pyramid.

5. User-Defined Function - Fibonacci:
   
   - Write a function `fibonacci(n)` that **returns the nth Fibonacci number** using recursion.
   
   #### Example:
```python
def fibonacci(n):
    # code 

fibonacci(0)  # Returns 0
fibonacci(1)  # Returns 1
fibonacci(5)  # Returns 5
```
   ✅ **Hints:** The Fibonacci sequence follows `F(n) = F(n-1) + F(n-2)`, 
   with base cases `F(0) = 0` and `F(1) = 1`.

