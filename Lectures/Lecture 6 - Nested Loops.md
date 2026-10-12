# Nested Loops in Python

## 1. What Is a Nested Loop?

A **nested loop** is a loop inside another loop. The inner loop executes completely for every iteration of the outer loop.

Nested loops can be used to work with patterns, rows and columns, and other problems that require repeated operations within repeated operations.

## 2. How Does a Nested Loop Work?

Consider the following structure:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

**Execution order:**

1. The outer loop assigns a value to `i`.
2. The inner loop executes all its iterations.
3. The outer loop moves to its next iteration.
4. The inner loop executes all its iterations again.
5. This continues until the outer loop finishes.

**Output:**

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

Notice that the inner loop executes **2 times for each iteration of the outer loop**.

## 3. Important Points to Remember

- The inner loop completes all its iterations before the outer loop moves to its next iteration.
- The outer loop controls how many times the inner loop is executed.
- The inner and outer loops can use different loop variables.
- The indentation determines which statements belong to each loop.
- The total number of inner-loop iterations is the number of outer-loop iterations multiplied by the number of inner-loop iterations per outer iteration, when both counts are fixed.

For example, if the outer loop executes 4 times and the inner loop executes 3 times per outer iteration, the statement inside the inner loop executes `4 * 3 = 12` times.

## 4. Nested Loops with Different Ranges

The inner loop does not always need to have the same number of iterations.

```python
for i in range(3):
    for j in range(i + 1):
        print("*", end="")
    print()
```

**Output:**

```text
*
**
***
```

Here, the number of inner-loop iterations depends on the current value of `i`.

**Key takeaway:** To understand a nested loop, trace the outer loop one iteration at a time and follow every iteration of the inner loop.
