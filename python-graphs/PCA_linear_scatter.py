import math
import random
from matplotlib import pyplot as plt
import numpy as np

# Number of points:
N = 50

# Parametrization:
r = np.random.uniform(0, 0.5, N)

# x:
x = np.linspace(1, 3, N)

# y:
y = x + r

# Line colour:
lineColour = '#282850'

# Points colour:
pointColour = '#B41414'

# Plot graph:
figure = plt.figure(figsize=(5, 5))
figureSubplot = figure.add_subplot(1,1,1)

# To plot the line:
plt.scatter(x, y, color=pointColour, marker='+', linewidth=1.0)
plt.axis('equal')

# Save plot:
filename = 'PCA_linear_scatter.png'
plt.savefig(filename, dpi = 150)
plt.show()
plt.close()
