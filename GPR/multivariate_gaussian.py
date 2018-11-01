mean = [0, 0, 0]
cov = [[1, 1, 0], [2, 5, 0], [0, 2, 2]]  # diagonal covariance

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = np.random.multivariate_normal(mean, cov, 5000).T
ax.scatter(x, y, z, 'x')
plt.axis('equal')

filename = 'multivariate_gaussian.png'
plt.savefig(filename, dpi = 150)
plt.show()
