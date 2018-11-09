## Imports
## -------
import george
import numpy as np
import matplotlib.pyplot as plt
import math

## Styles
## -------
csfont = {'fontname':'Lato', "weight": "medium"}
fnt = 22

## Code
## -------
x = np.array([-1.5, -1.2, -0.5, 0.5, 1.5])
yerr = np.zeros_like(x)
y = np.sin(2*x) + 1/(2*math.pi*0.5)**0.5 * math.e**((-(x + 1)**2)/(2*0.5**2))*5

# Plot data points:
plt.scatter(x, y)

# GP Kernel:
kernel = np.var(y) * george.kernels.ExpSquaredKernel(0.1)
gp = george.GP(kernel)
gp.compute(x, yerr)

x_pred = np.linspace(-2, 2, 100)
pred, pred_var = gp.predict(y, x_pred, return_var=True)
plt.fill_between(x_pred, pred - np.sqrt(pred_var), pred + np.sqrt(pred_var), color="k", alpha=0.2)
plt.plot(x_pred, pred, "k", lw=1.5, alpha=0.5)
plt.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)

# Real data model:
plt.plot(x_pred, np.sin(2*x_pred) + 1/(2*math.pi*0.5)**0.5 * math.e**((-(x_pred + 1)**2)/(2*0.5**2))*5, "--r", lineWidth=3)

plt.xlim(-2, 2)
plt.ylim(-1.2, 2.2)
plt.xlabel(r'x', fontsize=fnt, **csfont)
plt.ylabel(r'y', fontsize=fnt, **csfont)
filename = 'GPR_george.png'
plt.savefig(filename, dpi = 150)

plt.show()
