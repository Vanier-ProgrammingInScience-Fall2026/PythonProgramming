# Lab 3 — Functions

## Lab 3 Assignment

**Accept and access your assignment here:**

Important: Choose the Correct Section

There are three different assignment links, one for each section.

Please click ONLY the link that corresponds to your section.

-Do not use a link for another section.
Submitting your work through the wrong section may result in your grade being assigned incorrectly or not being recorded for your section.

Accept and access your assignment

Section 3:
https://classroom50.org/Vanier-ProgrammingInScience-Fall2026/programming-in-science-fall-2026/assignments/lab3-section-3/accept

Section 4:
https://classroom50.org/Vanier-ProgrammingInScience-Fall2026/programming-in-science-fall-2026/assignments/lab3-section-4/accept

Section 5:
https://classroom50.org/Vanier-ProgrammingInScience-Fall2026/programming-in-science-fall-2026/assignments/lab3-section-5/accept

Before clicking a link, make sure you select the link for your own section.


### 1. Open `lab3.py`

Open your Lab repository on your computer and open the file **`lab3.py`** in your Python editor, such as **PyCharm**.

### 2. Complete the Lab

Run your program several times and make sure that you get the expected output.

### 3. Save and Submit Your Work

When you are finished:

**a) Save and submit your work on GitHub**

1. Save your `lab3.py` file.
2. Copy the content of your completed file into `lab3.py` in your GitHub repository.
3. Save and commit your changes.
4. Push your changes to GitHub.

Your submission will be updated automatically when you push your changes.

**b) Upload a copy of `lab3.py` to Omnivox as well.**

> **Note:** Do not change the names of any files provided in the assignment. In particular, keep the file name `lab3.py` unchanged.

> **Note:** Do not change the name and content of any other files provided in the assignment, otherwise you will loose grade.


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

