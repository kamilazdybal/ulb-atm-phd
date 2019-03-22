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
font_title = 12
lineColour = '#f44242'

# Set hyperparameters:
lam = [0.1, 1, 5]
h = 0.1
mean = 10

x = np.arange(0, 20, 0.05)

# Display covariance matrix:
figure = plt.figure(figsize=(8, 5))

for idx, i in enumerate(lam):

    # Generate covariance matrix:
    Cov = covMatrix.covMatrixSE(x, h, i)

    # Draw realization from the current covariance:
    y = np.random.multivariate_normal(mean*np.ones(len(x)), Cov)

    # Append nRel number of realisations:
    nRel = 19
    for rel in range(1,1+nRel):
        y = np.append(y, np.random.multivariate_normal(10*np.ones(len(x)), Cov))

    figureSubplot = figure.add_subplot(1,3,idx+1)

    plt.hist(y, color=lineColour)
    figure.suptitle('Histograms from ' + str(nRel + 1) + ' realisations with mean = ' + str(mean), **csfont, fontsize=14)
    plt.title('$\lambda = ' + str(i) + '$', **csfont, fontsize=font_title)

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
filename = 'realisation-Histogram.png'
plt.savefig(filename, dpi = 150, bbox_inches='tight')
plt.show()
