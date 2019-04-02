## Imports
## -------
import george
import numpy as np
import matplotlib.pyplot as plt
import math

## Styles
## -------
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
font_label = 22
font_axis = 12

## Code
## -------
# Training input:
x = np.array([-1.5, -1.2, -0.5, 0.5, 1.5])

# Training output:
y = np.sin(2*x)

# 100 points for which we would like the GPR prediction:
x_pred = np.linspace(-2, 2, 100)

yerr = np.zeros_like(x)

# Plot data points:
figure = plt.figure(figsize=(11, 7))
figureSubplot = plt.subplot(1,1,1)
plt.scatter(x, y)

# GP Kernel:
kernel = np.var(y) * george.kernels.ExpSquaredKernel(0.1)
gp = george.GP(kernel)
gp.compute(x, yerr)

pred, pred_var = gp.predict(y, x_pred, return_var=True)
plt.fill_between(x_pred, pred - np.sqrt(pred_var), pred + np.sqrt(pred_var), color="k", alpha=0.2)
plt.plot(x_pred, pred, "k", lw=1.5, alpha=0.5)
plt.errorbar(x, y, yerr=yerr, fmt=".k", capsize=0)

# Real data model:
plt.plot(x_pred, np.sin(2*x_pred), "--r", lineWidth=3)
plt.xlim(-2, 2)
plt.ylim(-1.5, 1.5)
plt.xlabel(r'x', fontsize=font_label, **csfont)
plt.ylabel(r'y', fontsize=font_label, **csfont)

# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

filename = 'GPR-george.png'
plt.savefig(filename, dpi = 150)

plt.show()
