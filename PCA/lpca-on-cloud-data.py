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

# Data generation:
nPoints = 500
mean1 = [0,1] # data already centered
covariance1 = [[2, 0.5], [0.5, 0.5]]
x1, y1 = np.random.multivariate_normal(mean1, covariance1, nPoints).T

mean2 = [6, 4] # data already centered
covariance2 = [[3, 0.3], [0.3, 0.5]]
x2, y2 = np.random.multivariate_normal(mean2, covariance2, nPoints).T

X = np.column_stack((np.concatenate([x1, x2]), np.concatenate([y1, y2])))

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
idx = kmeans.labels_
centroids = kmeans.cluster_centers_
(PCs, eigvals, PC_scores) = lpca.local_pca(X, idx)

figureSubplot = plt.subplot(1,1,1)
plt.axis('equal')

# Plot division into clusters:
cmap = matplotlib.cm.get_cmap('Set2')

plt.scatter(X[:,0], X[:,1], c=cmap(idx), s=dataPointSize, marker='.')

origin = [centroids[0][0]], [centroids[0][1]]
plt.quiver(*origin, PCs[0][0,0], PCs[0][0,1], scale=30*(1-eigvals[0][0]), color=PCColour, width=0.005)
origin = [centroids[0][0]], [centroids[0][1]]
plt.quiver(*origin, PCs[0][1,0], PCs[0][1,1], scale=15*(1-eigvals[0][1]), color=PCColour, width=0.005)
origin = [centroids[1][0]], [centroids[1][1]]
plt.quiver(*origin, PCs[1][0,0], PCs[1][0,1], scale=30*(1-eigvals[1][0]), color=PCColour, width=0.005)
origin = [centroids[1][0]], [centroids[1][1]]
plt.quiver(*origin, PCs[1][1,0], PCs[1][1,1], scale=15*(1-eigvals[1][1]), color=PCColour, width=0.005)

plt.text(-1, 4, r'$k_1$', **csfont, fontsize=font_text, color=cmap(1), horizontalalignment='right')
plt.text(6, 7, r'$k_2$', **csfont, fontsize=font_text, color=cmap(0), horizontalalignment='right')

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
plt.savefig('lpca-on-cloud-data.png', dpi = 500, bbox_inches='tight')
plt.show()
