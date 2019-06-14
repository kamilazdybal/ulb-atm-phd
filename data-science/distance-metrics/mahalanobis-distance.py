# Two-dimensional demonstration of Mahalanobis distance
#
# References:
# C.M. Bishop - Pattern Recognition and Machine Learning
# http://mccormickml.com/2014/07/22/mahalanobis-distance/
#
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import distance

# Styles:
redColour = '#ffb69e'
blackColour = '#000000'
data_point = 0.5
new_point = 1
font_axis = 10
font_text = 12
font_title = 15
# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

# Data generation:
mean = [0, 0] # data already centered
covariance = [[2, 0.5], [0.5, 0.5]]
x, y = np.random.multivariate_normal(mean, covariance, 500).T
X = np.array([x,y])

figure1 = plt.figure(figsize=(6, 6))
figureSubplot = plt.subplot(1,1,1)
plt.axis('equal')
plt.scatter(x, y, color=redColour, marker='.', linewidth=data_point)
# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

# Show Euclidean and Mahalanobis distance:
plt.scatter(2,0, color=blackColour, marker='x', linewidth=new_point)
plt.scatter(0,2, color=blackColour, marker='x', linewidth=new_point)

euclidean_distance_1 = distance.euclidean([0, 0], [2, 0])
mahalanobis_distance_1 = distance.mahalanobis([0, 0], [2, 0], np.linalg.inv(covariance))
plt.text(2.2, 0.2, 'Euc: ' + '%s' % float('%.2g' % euclidean_distance_1), **hfont, fontsize=font_text)
plt.text(2.2, -0.2, 'Mah: ' + '%s' % float('%.2g' % mahalanobis_distance_1), **hfont, fontsize=font_text)

euclidean_distance_2 = distance.euclidean([0, 0], [0, 2])
mahalanobis_distance_2 = distance.mahalanobis([0, 0], [0, 2], np.linalg.inv(covariance))
plt.text(0.2, 2.2, 'Euc: ' + '%s' % float('%.2g' % euclidean_distance_2), **hfont, fontsize=font_text)
plt.text(0.2, 1.8, 'Mah: ' + '%s' % float('%.2g' % mahalanobis_distance_2), **hfont, fontsize=font_text)

plt.title('Euclidean and Mahalanobis distance comparison', **csfont, fontsize=font_title)
plt.savefig('mahalanobis-distance.png', dpi = 500, bbox_inches='tight')
plt.show()
