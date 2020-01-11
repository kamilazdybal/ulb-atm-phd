# LPCA on 2D data
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import distance
from sklearn.cluster import KMeans
import local_pca as lpca
import matplotlib

# Styles:
newPointColour = '#02111b'
PCColour = '#002f72'

dataPointSize = 5
data_point = 1
new_point = 1
font_axis = 10
font_text = 16
font_title = 15

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

k = 3

# Data generation:
nPoints = 500
mean1 = [0,1] # data already centered
covariance1 = [[0.4, 0.1], [0.1, 0.1]]
x1, y1 = np.random.multivariate_normal(mean1, covariance1, nPoints).T

x = np.linspace(0,4,nPoints)
y = -(x**2) + 7*x + 4
y = y + y1
x = x + x1

X = np.column_stack((np.concatenate([x]), np.concatenate([y])))

kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
idx = kmeans.labels_
centroids = kmeans.cluster_centers_
(PCs, eigvals, PC_scores) = lpca.local_pca(X, idx)

figure = plt.figure(figsize=(5, 7))
figureSubplot = plt.subplot(1,1,1)
plt.axis('equal')

# Plot division into clusters:
cmap = matplotlib.cm.get_cmap('Set2')

plt.scatter(X[:,0], X[:,1], c=cmap(idx), s=dataPointSize, marker='.')

for i in range(0,k):
    origin = [centroids[i][0]], [centroids[i][1]]
    plt.quiver(*origin, PCs[i][0,0], PCs[i][0,1], scale=40*(1-eigvals[i][0]), color=PCColour, width=0.005)
    origin = [centroids[i][0]], [centroids[i][1]]
    plt.quiver(*origin, PCs[i][1,0], PCs[i][1,1], scale=15*(1-eigvals[i][1]), color=PCColour, width=0.005)

plt.text(0.5, 17, r'$k_1$', **csfont, fontsize=font_text, color=cmap(1), horizontalalignment='right')
plt.text(3.5, 7, r'$k_3$', **csfont, fontsize=font_text, color=cmap(2), horizontalalignment='right')
plt.text(4, 12, r'$k_2$', **csfont, fontsize=font_text, color=cmap(0), horizontalalignment='right')

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

plt.subplots_adjust(wspace=0, hspace=0.4)
plt.savefig('lpca-on-nonlinear-data.png', dpi = 500, bbox_inches='tight')
plt.show()
