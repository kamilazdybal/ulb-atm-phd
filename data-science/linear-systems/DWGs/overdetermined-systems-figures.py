# Linear regression
# Between inputs x and targets y.

import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression

# Styles:
dataSetColour = '#012d4f'
PLSRegressionColour = '#ed303c'
borderColour = '#999999'
dataPointSize = 35
data_point = 1
new_point = 1
font_axis = 16
font_text = 20
font_title = 15

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

# Data generation:
x = np.array([1, 2])
y = x*0.9 + 1
x = x.reshape((-1, 1))
y = y.reshape((-1, 1))

# Plot the original inputs-targets:
figure1 = plt.figure(figsize=(8, 6))
figureSubplot = plt.subplot(1,1,1)
#plt.title('Original data set', **csfont, fontsize=font_title)
plt.axis('equal')
x_new = np.linspace(np.min(x) - 1, np.max(x) + 1, 100)
y_new = x_new * 0.9 + 1
plt.scatter(x, y, color=dataSetColour, marker='o', s=dataPointSize, zorder=2)
plt.plot(x_new, y_new, color=PLSRegressionColour, linewidth=2, zorder=1)
plt.text(0.3, 2, r'$(x_1, y_1)$', **csfont, fontsize=font_text, color=dataSetColour)
plt.text(2.1, 2.6, r'$(x_2, y_2)$', **csfont, fontsize=font_text, color=dataSetColour)

# Set the tick labels font:
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

figureSubplot.spines['bottom'].set_color(borderColour)
figureSubplot.spines['top'].set_color(borderColour)
figureSubplot.spines['left'].set_color(borderColour)
figureSubplot.spines['right'].set_color(borderColour)
figureSubplot.tick_params(axis='x')
figureSubplot.tick_params(axis='y')

plt.subplots_adjust(wspace=0, hspace=0.4)
plt.savefig('overdetermined-systems-figure-1.png', dpi = 200, bbox_inches='tight')
plt.show()
