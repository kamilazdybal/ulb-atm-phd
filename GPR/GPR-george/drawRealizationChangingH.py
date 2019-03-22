## Imports
import numpy as np
import matplotlib.pyplot as plt
import math

## Styles
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
font_label = 22
font_axis = 12
font_title = 22
lineColour = '#f44242'

# GP Kernel - Squared Exponential:
def kernelSE(x1, x2, h, lam):

    k12 = h**2*np.exp(-1.*(x1 - x2)**2/lam**2)

    return k12

# Covariance matrix from kernel:
def covKernel(x, h, lam):

    K = np.zeros((len(x), len(x)))

    for i in range(0, len(x)):
        for j in range (0, len(x)):

            K[i,j] = kernelSE(x[i], x[j], h, lam)

    return K

lam = 1
h = [0.1, 1, 5]

x = np.arange(0, 20, 0.01)

# Display covariance matrix:
figure = plt.figure(figsize=(10, 3))
for idx, i in enumerate(h):

    # Generate covariance matrix:
    Cov = covKernel(x, i, lam)

    # Draw realization from the current covariance:
    y = np.random.multivariate_normal(np.zeros(len(x)), Cov)

    # Plot:
    print(idx)
    figureSubplot = figure.add_subplot(1,3,idx+1)
    plt.plot(x, y, color=lineColour, linewidth=1)
    plt.title('$h = ' + str(i) + '$', **csfont, fontsize=font_title)

    # Set the tick labels font
    for label in (figureSubplot.get_xticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

    for label in (figureSubplot.get_yticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

plt.subplots_adjust(wspace=0.3, hspace=0.3)
filename = 'realizations-changing-h.png'
plt.savefig(filename, dpi = 300, bbox_inches='tight')

plt.show()
