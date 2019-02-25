"""
Dependent joint probability distribution

Documentation for `numpy.random.multivariate_normal`:

https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html
"""

import numpy as np
import matplotlib.pyplot as plt

# Styles:
pointColour = '#007277'
blackColour = '#000000'
data_point = 0.5
new_point = 1
font_axis = 10
font_text = 12
font_title = 14
# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

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

figure1 = plt.figure(figsize=(6, 6))
figureSubplot = plt.subplot(1,1,1)
plt.axis('equal')
plt.scatter(y1,y2, color=pointColour, marker='.', linewidth=data_point)
# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

plt.title('Joint probability distribution - dependent variables', **csfont, fontsize=font_title)

# Save plot:
filename = 'joint-probability-dependent.png'
plt.savefig(filename, dpi = 500, bbox_inches='tight')
plt.show()
plt.close()
