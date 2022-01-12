"""
15-1. Cubes: A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

x_s = range(1, 6)
y_s = [x**3 for x in x_s]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_s, y_s, edgecolor='red', s=40)

# Set chart title and label axes.
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
plt.show()

import matplotlib.pyplot as plt

x_s = range(1, 5001)
y_s = [x**3 for x in x_s]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_s, y_s, edgecolor='None', s=40)

# Set chart title and label axes.
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
ax.axis([0, 5500, 0, 133500000000])
plt.show()