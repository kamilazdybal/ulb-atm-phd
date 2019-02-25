"""
Independent joint probability distribution

Documentation for `numpy.random.normal`:

https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.normal.html
"""

import numpy as np
import matplotlib.pyplot as plt

# Styles:
pointColour = '#ff8247'
blackColour = '#000000'
data_point = 0.5
new_point = 1
font_axis = 10
font_text = 12
font_title = 14
# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

x1 = np.random.normal(1, 0.1, 5000)
x2 = np.random.normal(1, 0.1, 5000)

figure1 = plt.figure(figsize=(6, 6))
figureSubplot = plt.subplot(1,1,1)
plt.axis('equal')
plt.scatter(x1,x2, color=pointColour, marker='.', linewidth=data_point)
# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

plt.title('Joint probability distribution - independent variables', **csfont, fontsize=font_title)

# Save plot:
filename = 'joint-probability-independent.png'
plt.savefig(filename, dpi = 500, bbox_inches='tight')
plt.show()
plt.close()
