# This script draws Gaussian distribution.
import math
import matplotlib.pyplot as plt
import numpy as np

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
# Line colour:
lineColour = '#282850'
# Points colour:
fillColour = '#bacad1'

# Font sizes:
font_title = 16
font_axis = 12
font_labels = 16

# Number of points:
N = 200

# Mean:
mu = 0

# Deviation:
sigma = 0.5

# X-space:
x_start, x_end = -2, 2

# Define figureSubplotes:
x = np.linspace(x_start, x_end, N)


def y(x):
    return 1/(2*math.pi*sigma)**0.5 * math.e**((-(x - mu)**2)/(2*sigma**2))

figure = plt.figure(figsize=(10, 6))
figureSubplot = figure.add_subplot(1,1,1)
plt.title("Gaussian distribution with mean " + str(mu) + " and deviation " + str(sigma), **csfont, fontsize=font_title)
plt.xlabel('x', **csfont, fontsize=font_labels)
plt.ylabel('f(x)', **csfont, fontsize=font_labels)
plt.xlim(x_start, x_end)
plt.ylim(0, 0.7)

# To plot the line:
plt.plot(x, y(x), color=lineColour, linestyle='-', linewidth=2.0)

section = np.arange(-sigma, sigma, 1/100.)
plt.fill_between(section,y(section), facecolor=fillColour)
figureSubplot.set(xticks=[-sigma, sigma, 0], xticklabels=[r"$-\sigma$", r"$\sigma$", r"0"])

# Set the tick labels font:
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

# Save plot:
filename = 'gaussian-distribution.png'
plt.savefig(filename, dpi = 500, bbox_inches='tight')
plt.show()
plt.close()
