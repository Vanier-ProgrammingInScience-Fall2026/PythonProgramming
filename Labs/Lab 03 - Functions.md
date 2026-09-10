# Lab 3 — Functions

## Lab 3 Assignment

> **Note:** Upload your solution (only .py file) to Omnivox.


# Question 1 — Using Existing Functions

## Particle Distance

A particle moves from one point to another in a two-dimensional coordinate system.

The particle moves from point `(x1, y1)` to point `(x2, y2)`.

The distance between the two points is calculated using:

```text
d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

Write a Python program that:

1. Asks the user to enter `x1`.
2. Asks the user to enter `y1`.
3. Asks the user to enter `x2`.
4. Asks the user to enter `y2`.
5. Calculates the distance between the two points.
6. Rounds the distance to **2 decimal places**.
7. Finds the larger of `x1` and `x2` using the `max()` function.
8. Prints the distance and the larger x-coordinate.

## Required functions

For this question, use:

- `math.sqrt()`
- `round()`
- `max()`

You will need to import the `math` module.

## Example

```text
Enter x1: 2
Enter y1: 3
Enter x2: 8
Enter y2: 11

Distance: 10.0
Larger x-coordinate: 8.0
```

Another acceptable style of output could be:

```text
The distance is 10.0
The larger x-coordinate is 8.0
```

The exact wording is not important as long as the correct values are displayed.


---

# Question 2 — Writing Your Own Function

## Resultant Force

Two forces act on an object.

The magnitude of the resultant force is calculated using:

```text
FR = sqrt(F1^2 + F2^2 + 2 * F1 * F2 * cos(theta))
```

where:

- `F1` is the magnitude of the first force.
- `F2` is the magnitude of the second force.
- `theta` is the angle between the two forces, measured in degrees.
- `FR` is the magnitude of the resultant force.

## Part 1 — Create a function

Write a function called:

```python
def resultant_force(f1, f2, theta):
```

The function should:

1. Convert `theta` from degrees to radians.
2. Calculate the resultant force.
3. Return the resultant force.

Use:

- `math.radians()`
- `math.cos()`
- `math.sqrt()`

## Part 2 — Use your function

In the main part of the program:

1. Ask the user to enter the first force.
2. Ask the user to enter the second force.
3. Ask the user to enter the angle between the forces.
4. Call `resultant_force()`.
5. Print the resultant force rounded to **2 decimal places**.

## Example

```text
Enter the first force: 10
Enter the second force: 15
Enter the angle between the forces: 60

Resultant force: 21.79
```

Another example:

```text
Enter the first force: 5
Enter the second force: 5
Enter the angle between the forces: 90

Resultant force: 7.07
```

**Important:** The resultant-force calculation must be done inside the `resultant_force()` function.

---

