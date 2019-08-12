# Linear regression
# Between inputs x and targets y.

import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression

# Styles:
dataSetColour = '#3b8183'
PLSRegressionColour = '#ed303c'
borderColour = '#999999'
dataPointSize = 5
data_point = 1
new_point = 1
font_axis = 12
font_text = 20
font_title = 15

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

# Data generation:
nPoints = 500
mean = [0,1] # data already centered
covariance = [[1, 0.5], [0.5, 0.5]]
x, y = np.random.multivariate_normal(mean, covariance, nPoints).T
x = x.reshape((-1, 1))

# Perform Least-Squares regression:
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)

Y = x * model.coef_ + model.intercept_

# Plot the original inputs-targets:
figure1 = plt.figure(figsize=(8, 6))
figureSubplot = plt.subplot(1,1,1)
#plt.title('Original data set', **csfont, fontsize=font_title)
plt.axis('equal')
plt.scatter(x, y, color=dataSetColour, marker='.', s=dataPointSize)
plt.plot(x, Y, color=PLSRegressionColour, linewidth=2)
plt.text(np.min(x)+0.5, 0.8*np.max(y), 'Original data set', **csfont, fontsize=font_text, color=dataSetColour)
plt.text(0.2*np.max(x), np.min(y) + 0.5, 'Linear regression', **csfont, fontsize=font_text, color=PLSRegressionColour)

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
figureSubplot.tick_params(axis='x', colors=borderColour)
figureSubplot.tick_params(axis='y', colors=borderColour)

plt.subplots_adjust(wspace=0, hspace=0.4)
plt.savefig('linear-regression.png', dpi = 200, bbox_inches='tight')
plt.show()
