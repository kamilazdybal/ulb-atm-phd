import math
import random
from matplotlib import pyplot as plt
import numpy as np

# Number of points:
N = 100

# Radius:
r = 1

# Random radius bounds:
r_low = 0.9*r
r_up = 1.1*r

# Center:
x0 = 2
y0 = 2

# Parametrization:
t = np.linspace(0, 2*math.pi, N)
r = np.random.uniform(r_low, r_up, N)

# x:
x = x0 + r * np.cos(t)

# y:
y = y0 + r * np.sin(t)

# Line colour:
lineColour = '#282850'

# Points colour:
pointColour = '#B41414'

print(r)

# Plot graph:
figure = plt.figure(figsize=(5, 5))
figureSubplot = figure.add_subplot(1,1,1)

# To plot the line:
plt.scatter(x, y, color=pointColour, marker='+', linewidth=1.0)
plt.axis('equal')

# Save plot:
filename = 'PCA_circle.png'
plt.savefig(filename, dpi = 150)
plt.show()
plt.close()
