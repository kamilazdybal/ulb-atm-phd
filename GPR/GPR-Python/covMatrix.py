import numpy as np
import GPkernels

# Covariance matrix from kernel:
def covMatrixSE(x, h, lam):

    K = np.zeros((len(x), len(x)))

    for i in range(0, len(x)):
        for j in range (0, len(x)):

            K[i,j] = GPkernels.kernelSE(x[i], x[j], h, lam)

    return K
