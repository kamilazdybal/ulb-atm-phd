"""
Dependent joint probability distribution

Documentation for `numpy.random.multivariate_normal`:

https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1,0.01)

# Covariance kernel:
def squared_exponential_kernel(x1, x2, h, lam):
    """
    Squared Exponential Kernel
    """

    k12 = h**2*np.exp(-1.*(x1 - x2)**2/lam**2)

    return k12

# Covariance matrix:
def K(x, h, lam):
    """
    Populate covariance matrix using the covariance kernel
    """

    K = np.zeros((len(x), len(x)))

    for i in range(0, len(x)):
        for j in range(0, len(x)):

            K[i,j] = squared_exponential_kernel(x[i], x[j], h, lam)

    return K

K = K(x, 0.1, 0.1)

y1 = np.random.multivariate_normal(np.ones(len(x)), K)
y2 = np.random.multivariate_normal(np.ones(len(x)), K)

plt.scatter(y1,y2)
# plt.plot(x,y1, 'k-')
plt.axis('equal')

# Save plot:
filename = 'joint_probability_dependent.png'
plt.savefig(filename, dpi = 150)
plt.show()
plt.close()
