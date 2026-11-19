# Lecture 12: 3D Graphs and Animations

### **Table of Contents**

- [Lecture 12: 3D Graphs and Animations](#lecture-12-3d-graphs-and-animations)
    - [**Table of Contents**](#table-of-contents)
    - [1. **Introduction to 3D Graphics**](#1-introduction-to-3d-graphics)
    - [2. **Creating 3D Plots with Matplotlib**](#2-creating-3d-plots-with-matplotlib)
      - [Basic Syntax for Creating a 3D Plot:](#basic-syntax-for-creating-a-3d-plot)
      - [Example: Plotting a 3D Scatter Plot](#example-plotting-a-3d-scatter-plot)
      - [Example: Plotting a 3D Scatter Plot on Google.Colab](#example-plotting-a-3d-scatter-plot-on-googlecolab)
      - [3D Line Plot:](#3d-line-plot)
    - [3. **Creating Animations with Matplotlib**](#3-creating-animations-with-matplotlib)
      - [Example: Simple Line Animation](#example-simple-line-animation)

### 1. **Introduction to 3D Graphics**

**3D graphics** represent data along X, Y, and Z axes. This extra dimension can reveal relationships involving several variables, including results from scientific simulations, physical models, and geographic data.

In Python, **Matplotlib** provides the tools for creating these visualizations. Its `mpl_toolkits.mplot3d` module supplies the 3D axes used by the plotting examples in this lecture.

### 2. **Creating 3D Plots with Matplotlib**

To create a 3D plot, import Matplotlib and create an axes object with a 3D projection. The resulting axes can display points, lines, and surfaces in three dimensions.

#### Basic Syntax for Creating a 3D Plot:
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()

# Add 3D axes to the figure
ax = fig.add_subplot(projection='3d')

# Plot data points (example)
ax.scatter(x, y, z)  # Where x, y, z are lists or arrays of data points

# Display the plot
plt.show()
```

#### Example: Plotting a 3D Scatter Plot
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data points
x = np.random.rand(100) # uniformly
y = np.random.rand(100)
z = np.random.rand(100)

# Create a figure
fig = plt.figure()

# Add 3D axes to the figure
ax = fig.add_subplot(projection='3d')

# Plot data points
ax.scatter(x, y, z)

# Set labels for the axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the plot
plt.show()
```

This creates a 3D scatter plot where the data points are randomly distributed along the X, Y, and Z axes.

#### Example: Plotting a 3D Scatter Plot on Google.Colab

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data points
X = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(X, y, z, c=z, cmap="viridis", label="data", s=50)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()
```

#### 3D Line Plot:
You can also plot 3D lines using the `plot()` function in 3D space.

Example:
```python
# Define data for 3D line plot

# Generates a fixed number of evenly spaced values between start and stop.
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot the 3D line
ax.plot(x, y, z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the plot
plt.show()
```

### 3. **Creating Animations with Matplotlib**

**Animations** allow you to display changing data over time, making your visualizations more dynamic and engaging. In Python, **Matplotlib** provides the `FuncAnimation` class from the `matplotlib.animation` module to create animations.

#### Example: Simple Line Animation
Here’s a basic example that animates a sine wave:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Pre-allocate Figure and Axis
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# 2. Use a persistent line object
line, = ax.plot([], [], lw=2, color='teal')
ax.set_xlim(0, 2 * np.pi)   # set the range of x label
ax.set_ylim(-1.1, 1.1)      # set the range of y label
ax.grid(True, linestyle='--', alpha=0.6) # alpha is the transparency (0: transparent, 1: opaque)
ax.set_title("Smoother Sine Wave Animation")

# 3. Efficient Update Function
def update(frame):
    # Only update the data, don't redraw the whole axis
    line.set_data(x[:frame], y[:frame])
    return line,

# 4. Create Animation
# interval=20 (1000/20=50 FPS) makes it feel much smoother
# blit=True uses the technology of screenshoting the previous frame when draw a new frame 
ani = FuncAnimation(fig, update, frames=len(x), interval=20, blit=True)

# save the animation as a gif file (requres pillow library)
ani.save('sine_wave.gif', writer='pillow', fps=30)

plt.show()
```

This code animates a sine wave, showing the graph's development frame by frame.
