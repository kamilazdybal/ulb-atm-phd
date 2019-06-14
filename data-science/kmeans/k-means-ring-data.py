# This is a demo of K-means clustering
# A data set which has a ring shape is separated into two clusters

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import distance
from sklearn.cluster import KMeans

# Styles:
dataSetColour = '#838383'
cluster1Colour = '#40e0d0'
cluster2Colour = '#ffb993'
newPointColour = '#02111b'
dataPointSize = 5
data_point = 1
new_point = 1
font_axis = 10
font_text = 12
font_title = 15

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

# Data generation:
nPoints = 500
mean1 = [0,0] # data already centered
covariance1 = [[4, 0], [0, 4]]
x1, y1 = np.random.multivariate_normal(mean1, covariance1, nPoints).T

# Generate ring from data:
def dataRing(xy):
    dataRing = []
    for point in xy:
        point = np.array(point)
        dataRing.append(point / 10 + point / np.linalg.norm(point))
    return dataRing

xy = zip(x1, y1)
X = np.array(dataRing(xy))

figure1 = plt.figure(figsize=(5, 8))
figureSubplot = plt.subplot(3,1,1)
plt.title('Original data set', **csfont, fontsize=font_title)
plt.axis('equal')
plt.scatter(X[:,0], X[:,1], color=dataSetColour, marker='.', s=dataPointSize)

# Set the tick labels font:
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

# Perform K-means clustering:
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
y_kmeans = kmeans.predict(X)
idx = kmeans.labels_
centroids = kmeans.cluster_centers_

figureSubplot = plt.subplot(3,1,2)
plt.title('Data set clustering using K-means', **csfont, fontsize=font_title)
plt.axis('equal')
# Plot division into clusters:
plt.scatter(X[:,0], X[:,1], c=y_kmeans, s=dataPointSize, cmap='Pastel2', marker='.')

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], color=newPointColour, marker='x', lineWidth=data_point, s=20);

for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

# Classify new points:
newPoints = np.array([[0,0], [1,1], [0.5, 0.5], [0.5, 0], [-0.5, -0.5], [3, 0], [-3, 1]])
prediction = kmeans.predict(newPoints)

figureSubplot = plt.subplot(3,1,3)
plt.title('Classification of new data points', **csfont, fontsize=font_title)
plt.axis('equal')
plt.scatter(X[:,0], X[:,1], c=y_kmeans, s=dataPointSize, cmap='Pastel2', marker='.')
plt.scatter(newPoints[:,0], newPoints[:,1], c=prediction, cmap='Dark2', marker='o', s=20, lineWidth=data_point)
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

plt.subplots_adjust(wspace=0, hspace=0.4)
plt.savefig('k-means-ring-data.png', dpi = 500, bbox_inches='tight')
plt.show()
