"""
Independent joint probability distribution

Documentation for `numpy.random.normal`:

https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(1, 0.1, 5000)
x2 = np.random.normal(1, 0.1, 5000)

plt.scatter(x1,x2)
plt.axis('equal')

# Save plot:
filename = 'joint_probability_independent.png'
plt.savefig(filename, dpi = 150)
plt.show()
plt.close()
