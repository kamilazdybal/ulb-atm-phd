## Imports
import numpy as np
import matplotlib.pyplot as plt
import math
import covMatrix

## Styles
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
font_label = 22
font_axis = 12
font_title = 22
lineColour = '#f44242'

# Set hyperparameters:
lam = [0.1, 1, 5]
h = 0.1
mean = 1

x = np.arange(0, 20, 0.05)

# Display covariance matrix:
figure = plt.figure(figsize=(10, 6))

for idx, i in enumerate(lam):

    # Generate covariance matrix:
    Cov = covMatrix.covMatrixSE(x, h, i)

    # Draw realization from the current covariance:
    y = np.random.multivariate_normal(mean*np.ones(len(x)), Cov)

    figureSubplot = figure.add_subplot(2,3,idx+1)
    im = plt.imshow(Cov)
    plt.yticks([]), plt.xticks([])
    plt.title('$\lambda = $' + str(i), **csfont, fontsize=font_title)
    cb = plt.colorbar(im, fraction=0.046, pad=0.04)
    plt.clim(0,h**2)
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    # Set the tick labels font
    for label in (figureSubplot.get_xticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

    for label in (figureSubplot.get_yticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

    figureSubplot = figure.add_subplot(2,3,idx+4)
    plt.plot(x, y, color=lineColour, linewidth=1)

    # Set the tick labels font
    for label in (figureSubplot.get_xticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

    for label in (figureSubplot.get_yticklabels()):
        label.set_fontname('Charter')
        label.set_fontweight('regular')
        label.set_fontsize(font_axis)

plt.subplots_adjust(wspace=0.3, hspace=0.2)
filename = 'cov-Kernel-SE-changing-lambda.png'
plt.savefig(filename, dpi = 300, bbox_inches='tight')
plt.show()
