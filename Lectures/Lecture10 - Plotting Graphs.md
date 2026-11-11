# Lecture 10: Plotting Graphs

### **Table of Contents**

1. [**Introduction to NumPy**](#1-introduction-to-numpy)
2. [**Introduction to Plotting in Python**](#2-introduction-to-plotting-in-python)
3. [**Creating Density Plots**](#3-creating-density-plots)
4. [**Basic Image Processing For Fun**](#4-basic-image-processing-for-fun)
5. [**Debugging and Testing Plotting Operations**](#5-debugging-and-testing-plotting-operations)

## 1. **Introduction to NumPy**

NumPy is a Python library for efficient numerical arrays and matrices. It also provides mathematical operations designed to work over entire arrays, making it a foundation for many scientific-computing tools.

### 1.0 Installation

Install NumPy from a terminal with:

``` bash
pip install numpy
```


For mac, you might need to execute additional command:

```bash
python3 -m venv venv  
source venv/bin/activate   
pip install numpy
```

### 1.1 **Why NumPy?**

- Stores and processes numerical data efficiently.
- Supports vectorized operations, which often avoid explicit Python loops.
- Provides core functionality for scientific computing and data analysis.

---

### 1.2 NumPy Array vs. Python List

- A **Python list** can hold elements of different types (e.g., numbers, strings).
- A **NumPy array** is more efficient because all elements are stored as the same type (usually numbers).
- NumPy arrays use less memory and allow faster mathematical operations compared to lists.

Example:

```python
import numpy as np

py_list = [1, 2, 3]
np_array = np.array([1, 2, 3])

print(py_list)   # [1, 2, 3]
print(np_array)  # [1 2 3]
```

With lists, operations are slower:

```python
[1, 2, 3] * 2     # [1, 2, 3, 1, 2, 3]
```

With NumPy arrays, math is direct:

```python
np.array([1, 2, 3]) * 2   # [2 4 6]
```

---

### 1.3. Generating Data with NumPy

NumPy has many built-in functions to generate arrays and random data.

#### 1.3.1 Basic Array Creation

```python
import numpy as np

# Create an array of numbers from 0 to 9
arr = np.arange(10)
print(arr)

# Create an array of 5 zeros
zeros = np.zeros(5)
print(zeros)

# Create an array of 5 ones
ones = np.ones(5)
print(ones)
```

### 1.4 Random Data Generation

NumPy can generate random numbers from different **distributions**:

- **Uniform distribution**

```python
np.random.uniform(0, 10, 5)  # 5 numbers between 0 and 10
```

- **Normal (Gaussian) distribution**

```python
np.random.normal(0, 1, 5)  # mean=0, std=1, 5 samples
```

- **Poisson distribution**

```python
np.random.poisson(3, 5)  # lambda=3, 5 samples
```

---

### 1.5. Statistics with NumPy

NumPy makes it easy to calculate basic statistics:

```python
data = np.array([1, 2, 3, 4, 5])

print(np.mean(data))   # Average
print(np.median(data)) # Median
print(np.std(data))    # Standard deviation
print(np.var(data))    # Variance (std ^ 2)
print(np.min(data))    # Minimum
print(np.max(data))    # Maximum
```

## 2. **Introduction to Plotting in Python**

Plotting data is a critical aspect of data analysis and visualization. Python provides several libraries for plotting graphs, and the most popular one is **Matplotlib**. The **matplotlib.pyplot** module provides a set of functions for creating various types of graphs, such as line plots, scatter plots, bar charts, and more.

In this lecture, we will focus on two important aspects of plotting:
- **Simple line plots** using `plot()` and `show()`.
- **Density plots**, which visualize the distribution of data.

To get started with plotting, you first need to install and import **Matplotlib**. If you don’t have it installed, you can install it using the following command:
```bash
pip install matplotlib
```

Then, import **Matplotlib** in your code:
```python
import matplotlib.pyplot as plt
```

### 2.1. **Plotting Simple Graphs Using `plot()` and `show()`**

The **plot()** function is used to create line plots in Matplotlib. You can use this function to plot data points on a graph, and the **show()** function is used to display the plot.

#### Basic Syntax of `plot()` and `scatter()`:
```python
plt.plot(x, y)  # x and y are lists or arrays of data points
plt.scatter(x, y)
```

#### `show()` Function:
After creating the plot with `plot()`, use `plt.show()` to display the graph.

#### Example: Plotting a Simple Line Graph
```python
import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y)

# Display the plot
plt.show()
```

This code will create a simple line plot with `x` values on the x-axis and `y` values on the y-axis.

#### Adding Labels and Title:
You can customize your plot by adding a title and labels for the axes.

Example:
```python
# marker highlights each data point
# label will be displayed when plt.legend() is executed
plt.plot(x, y, marker="o", label="A simple line plot: x-y")
plt.plot(y, x, marker="x", label="A simple line plot: y-x")
plt.title('Simple Line Plot')  # Adding a title
plt.xlabel('X Values')  # Adding a label for the x-axis
plt.ylabel('Y Values')  # Adding a label for the y-axis
plt.legend()        # display the labels 
plt.show()
```

### 3. **Creating Density Plots**

A **Density Plot** is a smooth representation of the distribution of a dataset. It provides a more continuous representation of the data's distribution compared to histograms. In Matplotlib, you can use **Seaborn**, another library built on top of Matplotlib, to create density plots. Seaborn provides a more convenient interface for complex plotting.

If you don't have Seaborn installed, you can install it with:
```bash
pip install seaborn
```

#### Basic Syntax for Density Plot:
```python
import seaborn as sns
sns.kdeplot(data)
```

Here, **`kdeplot`** stands for Kernel Density Estimation Plot, which is used to visualize the data distribution.

#### Example: Creating a Density Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data: Normally distributed data
import numpy as np
data = np.random.normal(size=1000)

# Create the density plot
sns.kdeplot(data)

# Display the plot
plt.show()
```

In this example, `data` is a sample of 1000 random values drawn from a normal distribution. The **`kdeplot()`** function generates the density plot, which will show the smooth distribution of the data.

#### Customizing the Density Plot:
You can customize the appearance of the density plot by changing its color, style, and bandwidth (which controls the smoothness of the plot).

Example with customizations:
```python
sns.kdeplot(data, color='green', fill=True, bw_adjust=0.5)  # Adjust the bandwidth for smoothness
plt.show()
```

- **`color`**: Sets the color of the plot.
- **`fill`**: Fills the area under the curve with color.
- **`bw_adjust`**: Adjusts the bandwidth, which controls the smoothness of the density plot.

### 4 Basic Image Processing For Fun

Image processing is a natural next step after learning NumPy and Matplotlib, because images are just arrays of pixel values. 

mages can be represented as NumPy arrays:
- A grayscale image is a 2D array (height × width).
- A color image is a 3D array (height × width × 3 for RGB).

Example: Loading and displaying an image

``` python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load image with Pillow
img = Image.open("example.jpg")

# Convert to NumPy array
img_array = np.array(img)

print(img_array.shape)  # e.g. (300, 400, 3)

# Display image
plt.imshow(img_array)
plt.axis("off")
plt.show()
```

```python
# Convert to grayscale
gray = np.mean(img_array, axis=2)

# darker
gray -= 50

# brighter
gray += 100

# crop rows
gray = gray[50: -50]

# crop cols
gray = gray.T[50:-50].T         # T is transpose, row <-> column

plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.axis("off")
plt.show()
```

### 5. **Debugging and Testing Plotting Operations**

When working with plots, it's essential to ensure that your data is correctly formatted and that your plotting functions are used properly. Here are some debugging tips:

#### Checking Data:
Ensure your data is in the correct format (e.g., lists or arrays) and contains no missing or invalid values.
```python
# Check the type and shape of your data
print(type(x), len(x))  # Ensure x is a list or array and has the correct length
```

#### Handling Errors in Plotting:
- **Empty data**: Make sure that your data is not empty.
- **Mismatched dimensions**: Ensure that the x and y data points have the same length when plotting.

Example of checking for empty data:
```python
if len(x) == 0 or len(y) == 0:
    print("Error: Data is empty")
else:
    plt.plot(x, y)
    plt.show()
```

#### Testing Plot Appearance:
- **Labels and title**: Ensure that your labels and titles are correctly placed and readable.
- **Adjusting figure size**: If the plot appears too small or too large, you can adjust the figure size using:
```python
plt.figure(figsize=(8, 6))  # Adjust the figure size (width, height)
```

Example with figure size adjustment:
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Custom Plot with Adjusted Size')
plt.show()
```

#### Testing Density Plot:
- Make sure the data you're passing to the **`kdeplot()`** function is numeric and has a reasonable distribution.
- You can use `np.random.normal()` or `np.random.uniform()` to create sample datasets for testing.

Example:
```python
import numpy as np
data = np.random.normal(size=500)
sns.kdeplot(data)
plt.show()
```

### 1.4 Random Data Generation with NumPy - More details

Sometimes, we need numerical data to perform experiments, simulations,
or analysis. Instead of entering data manually, we can use NumPy to
generate random numbers.

NumPy provides different functions to generate random data. In this
section, we will learn about three common distributions.

## 1. Uniform Distribution -- `np.random.uniform()`

A uniform distribution generates random numbers within a specified
range, where every value in that range has an equal chance of being
selected.

**Syntax:**

``` python
np.random.uniform(minimum, maximum, size)
```

**Example:**

``` python
import numpy as np

data = np.random.uniform(0, 10, 5)

print(data)
```

Possible output:

``` text
[2.34 8.91 4.56 0.72 6.18]
```

**Parameters:**

-   `minimum`: The lower limit of the range.
-   `maximum`: The upper limit of the range (normally excluded).
-   `size`: The number of random values to generate.

**Real-life example:** Generating five random temperatures between 0 and
10 degrees.

## 2. Normal Distribution -- `np.random.normal()`

A normal distribution generates random numbers that tend to be
concentrated around an average value (mean).

In real life, many measurements follow approximately a normal
distribution. For example, people's heights, test scores, and
measurement errors often tend to be distributed around an average.

**Syntax:**

``` python
np.random.normal(mean, standard_deviation, size)
```

**Example:**

``` python
import numpy as np

heights = np.random.normal(170, 10, 100)

print(heights)
```

**Parameters:**

-   `mean`: The average value around which the numbers are distributed.
-   `standard_deviation`: Determines how spread out the values are
    around the average.
-   `size`: The number of random values to generate.

**Understanding standard deviation:**

-   A small standard deviation means most values are close to the
    average.
-   A large standard deviation means values are more spread out.

For example:

``` python
data1 = np.random.normal(170, 5, 1000)
data2 = np.random.normal(170, 20, 1000)
```

Both datasets have an average of 170, but `data2` has more variation.

## 3. Poisson Distribution -- `np.random.poisson()`

A Poisson distribution generates random whole numbers representing how
many times an event happens within a fixed interval.

It is useful when we want to simulate the number of occurrences of an
event over a period of time or within a specific area.

**Real-life examples:**

-   Number of customers entering a store per minute.
-   Number of cars passing through a road per minute.
-   Number of emails received per hour.
-   Number of patients arriving at a hospital per hour.

**Syntax:**

``` python
np.random.poisson(lam, size)
```

**Example:**

``` python
import numpy as np

cars = np.random.poisson(4, 10)

print(cars)
```

Possible output:

``` text
[2 4 3 1 5 2 3 4 2 6]
```

**Parameters:**

-   `lam` (Lambda, λ): The expected average number of times an event
    happens within a fixed interval.
-   `size`: The number of random values to generate.

**Understanding Lambda (λ):**

We must specify lambda before generating the random data. Its value can
come from:

-   **Real data:** We collect historical data and calculate the average
    number of occurrences per interval.
-   **Simulation:** We choose a reasonable average based on our
    assumptions or the situation we want to simulate.

For example, suppose we know that an average of 4 cars pass through a
road every minute.

``` python
cars = np.random.poisson(4, 10)
```

Here:

-   `4`: On average, 4 cars pass per minute.
-   `10`: We simulate 10 different minutes.

The generated values represent the number of cars passing during each
minute.

**Important:** Lambda does not mean that exactly 4 events will happen in
every interval. It represents the expected average over many intervals.
Some minutes might have 2 cars, others 5 or 6.

------------------------------------------------------------------------

## Summary: Comparing the Three Distributions

  -----------------------------------------------------------------------
  Distribution            What does it generate?  Example
  ----------------------- ----------------------- -----------------------
  Uniform                 Random values within a  Temperature between 0
                          range, equally likely   and 10

  Normal                  Values concentrated     People's heights
                          around an average       

  Poisson                 Number of occurrences   Cars passing per minute
                          of an event             
  -----------------------------------------------------------------------

**Remember:**

-   **Uniform:** Every value within the specified range has an equal
    chance.
-   **Normal:** Values tend to be around an average.
-   **Poisson:** We count how many times an event happens within a fixed
    interval.

