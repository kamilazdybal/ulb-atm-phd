import numpy as np

# GP Kernel - Squared Exponential:
def kernelSE(x1, x2, h, lam):

    k12 = h**2*np.exp(-1.*(x1 - x2)**2/lam**2)

    return k12
