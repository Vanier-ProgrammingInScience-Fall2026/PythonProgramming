# Lab 1 — Input and Output

## Lab 1 Assignment

**Accept and access your assignment here:**

https://classroom50.org/Vanier-ProgrammingInScience-Fall2026/programming-in-science-fall-2026/assignments/lab1-section-3/accept


1. Open lab1.py

Open your Lab 1 repository on your computer and open the file lab1.py in your Python editor (such as PyCharm).

2. Complete the Lab

Complete Task 1 and Task 2 in lab1.py.

Run your program several times and make sure that you get the expected output.

3. Save and Submit Your Work

When you are finished:
a)
Save your lab1.py file.
Copy its content in lab1.py under your github repository.
save and Commit your changes.

Your submission will be updated automatically when you push your changes.

b)upload a copy of lab1.py to Omnivox as well.

---

## Task 1 — Hello World

Write a Python program that prints exactly:

```text
Hello, World!
```

You should use the `print()` function.

### Expected Output

```text
Hello, World!
```

---

## Task 2 — Input and Output with Different Variable Types

Write a Python program that asks the user to enter:

1. Their **name** — a string
2. Their **age** — an integer
3. Their **height in meters** — a float

Store each value in an appropriate variable.

Your program should then display the information using the following format:

```text
Hello, Alice!
You are 25 years old.
Your height is 1.75 meters.
```

### Example Interaction

```text
Enter your name: Alice
Enter your age: 25
Enter your height (meters): 1.75
Hello, Alice!
You are 25 years old.
Your height is 1.75 meters.
```

Your program should work with different names, ages, and heights.

For example, if the user enters:

```text
Bob
30
1.80
```

the output should be:

```text
Hello, Bob!
You are 30 years old.
Your height is 1.8 meters.
```

---

## Requirements

Your program must:

- Use `print()` to display output.
- Use `input()` to get information from the user.
- Store the name in a variable.
- Convert the age to an integer using `int()`.
- Convert the height to a floating-point number using `float()`.
- Complete both tasks in the same file: `lab1.py`.

You **do not need to use functions or f-strings** for this lab.

---

## Running Your Program

Open the terminal in VS Code and run:

```text
python lab1.py
```

Follow the prompts and enter your information.

---

## Running the Tests

Your assignment repository contains tests for Lab 1.

Run the tests with:

```text
pytest
```

or:

```text
python -m pytest
```

Make sure all tests pass before submitting your work.

---

## Submission

Your Lab 1 assignment is submitted through **Classroom50**.

After completing your work:

1. Save your changes.
2. Run your program and make sure it works.
3. Run `pytest` and make sure all tests pass.
4. Commit your changes.
5. Push your changes to GitHub.

For example:

```text
git add .
git commit -m "Complete Lab 1"
git push
```

Your submission will be updated when you push your changes.

---

## What You Should Submit

Your assignment repository should contain your completed:

```text
lab1.py
```

You do **not** need to upload the file separately to Omnivox unless your instructor specifically asks you to do so.

Good luck with Lab 1! 🐍
