# Lecture 9: File I/O

### **Table of Contents**

- [Lecture 9: File I/O](#lecture-9-file-io)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Introduction to File I/O**](#1-introduction-to-file-io)
    - [2. **Working with TXT Files**](#2-working-with-txt-files)
      - [Reading from a TXT File:](#reading-from-a-txt-file)
      - [Writing to a TXT File:](#writing-to-a-txt-file)
    - [3. **Working with CSV Files**](#3-working-with-csv-files)
      - [Reading from a CSV File:](#reading-from-a-csv-file)
      - [Writing to a CSV File:](#writing-to-a-csv-file)
    - [4. **Reading an Array from a File**](#4-reading-an-array-from-a-file)
      - [Reading an Array from a TXT File:](#reading-an-array-from-a-txt-file)
      - [Reading an Array from a CSV File:](#reading-an-array-from-a-csv-file)
    - [5. **Debugging and Testing File I/O Operations**](#5-debugging-and-testing-file-io-operations)
      - [Debugging File Opening:](#debugging-file-opening)
      - [Debugging Data Parsing:](#debugging-data-parsing)

### 1. **Introduction to File I/O**

File **Input/Output (I/O)** lets a program read external data and save results for later use. It is useful whenever information must persist after the program stops or must be processed from an existing file.

Python handles files with built-in tools such as **`open()`**. The mode controls the operation: `r` reads, `w` writes, and `a` appends.

Basic Syntax to open a file:
```python
# Open the file in read mode
file = open('filename.txt', 'r')  

file = open('C:/Users/niloufar/Downloads/filename.txt', 'r')  # absolute path with '/'

file = open('C:\\Users\\niloufar\\Downloads\\filename.txt', 'r')  # absolute path with '\\'
```

The filename may also be an absolute path, such as `'C:/Users/wangy/Downloads/filename.txt'`. In Windows paths, use `/` or escape each backslash as `\\`.

After opening a file, read from it or write to it and then call `file.close()`. Leaving a file open can prevent data from being flushed and may leave the file locked.

Another way to open a file is to use the keyword `with...as`, in this way, python will automatically close the file without using `file.close()`.

```python
with open('filename.txt', 'r') as file:
```

### 2. **Working with TXT Files**

**TXT files** are plain text files that contain unformatted data. Reading and writing to TXT files is straightforward in Python. You can read the entire contents of a file or read it line by line.

#### Reading from a TXT File:
To read from a TXT file, use the `open()` function in **read mode (`'r'`)**.

Example: Reading the contents of a TXT file:
```python
# Open the file in read mode
file = open('data.txt', 'r')

# Read the entire file content
content = file.read()
print(content)

# Close the file
file.close()
```

or 

```python
with open('data.txt', 'r') as file:
    print(file.read())

# no need to close the file manually
```

You can also read the file line by line:
```python
file = open('data.txt', 'r')

# Read each line of the file
for line in file:
    print(line.strip())  # .strip() removes any leading/trailing whitespace

file.close()
```

or 

```python
with open('data.txt', 'r') as file:
    for line in fiel:
        print(line.strip())  # .strip() removes any leading/trailing whitespace
```

#### Writing to a TXT File:
To write data to a TXT file, open the file in **write mode (`'w'`)**.

Example: Writing to a file:
```python
file = open('output.txt', 'w')

# Write data to the file
file.write("Hello, World!\n")
file.write("This is a second line.")

file.close()
```

or 
```python
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.")
```

Note: If the file already exists, it will be overwritten. Use **append mode (`'a'`)** if you want to add data without overwriting.

### 3. **Working with CSV Files**

**CSV files** (Comma-Separated Values) are used to store tabular data in a text format. Each line represents a row, and the values within each row are separated by commas. CSV files are widely used for data storage and sharing.

To work with CSV files in Python, you can use the **`csv` module**. This module provides functions to read from and write to CSV files.

#### Reading from a CSV File:
The `csv.reader()` function is used to read a CSV file. It returns each row as a list of values.

Example: Reading from a CSV file:
```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

In this example, `reader` is an iterable that yields each row of the CSV file as a list.

#### Writing to a CSV File:
The `csv.writer()` function is used to write data to a CSV file. You can pass a list of values, and the writer will convert them into a comma-separated format.

Example: Writing to a CSV file:
```python
import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Name', 'Age', 'City'])
    # Write data
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
```

Note: Always specify `newline=''` when opening the file in write mode to avoid extra blank lines in the output.

### 4. **Reading an Array from a File**

You can store an array of data in a file and read it back into your program. Arrays are commonly represented in text files, and the data can be read and converted into an array or list in Python.

#### Reading an Array from a TXT File:
If you have a list of numbers in a TXT file (one number per line), you can read them into a list.

Example: Reading an array from a TXT file:
```python
# Assume 'numbers.txt' contains one number per line
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    
print(numbers)
```

This code reads each line from the file, strips any leading or trailing whitespace, converts the line to an integer, and stores it in the `numbers` list.

#### Reading an Array from a CSV File:
If you have a CSV file containing numerical data, you can read it into a 2D array (list of lists) by treating each row as an array of values.

Example: Reading a 2D array from a CSV file:
```python
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    array = [list(map(int, row)) for row in reader]  # Convert each row to a list of integers
    
print(array)
```

Here, the `map()` function is used to convert each string in the CSV row to an integer, and each row is added as a sublist in the final array.

### 5. **Debugging and Testing File I/O Operations**

When working with file I/O, it’s important to ensure that files are correctly opened, read, written, and closed. Below are some debugging techniques for handling file I/O operations:

#### Debugging File Opening:
Ensure that the file exists and that the correct file path is used.
```python
try:
    file = open('data.txt', 'r')
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File not found.")
```

#### Debugging Data Parsing:
When reading data into arrays or lists, check that the data is correctly parsed. Use print statements to verify that the data read from the file matches the expected format.

Example:
```python
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]
    print("Read numbers:", numbers)
```

Test with files containing edge cases, such as empty files or files with inconsistent formatting.
