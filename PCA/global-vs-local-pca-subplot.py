# LPCA on 2D data
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import distance
from sklearn.cluster import KMeans
import local_pca as lpca
import matplotlib
from sklearn.decomposition import PCA
from matplotlib import rc
from matplotlib import gridspec

# Styles:
global_color = '#7b8280'
PCColour = '#000000'

parula_1 = (0.2422, 0.1504, 0.6603)
parula_2 = (0.9769, 0.9839, 0.0805)

dataPointSize = 15
data_point = 1
new_point = 1
font_axis = 10
font_text = 20
font_title = 15
ln = 1
nPoints = 1000

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}

figure = plt.figure(figsize=(13, 4))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])
# First subplot
figureSubplot = plt.subplot(gs[0])

# Generate randomized dataset with linearity
q = 1
# Data generation:

mean1 = [0,1] # data already centered
covariance1 = [[3.4, 1.1], [1.1, 2.1]]
x1, y1 = np.random.multivariate_normal(mean1, covariance1, nPoints).T

y = np.linspace(0,4,nPoints)
x = -(y**2) + 7*y + 4
y = y + y1
x = x + x1

Dataset = np.column_stack((np.concatenate([x]), np.concatenate([y])))
Dataset_proc = Dataset - np.mean(Dataset, axis=0)

# Perform PCA
pca = PCA()
pca.fit(Dataset)
scores = pca.transform(Dataset)
PCs = pca.components_
eigvals = pca.explained_variance_ratio_

Dataset_projected = np.dot(Dataset_proc, np.transpose(pca.components_[:q,:]))
Dataset_approx = np.dot(pca.transform(Dataset)[:,:q], pca.components_[:q,:]) + np.mean(Dataset, axis=0)

plt.scatter(Dataset_proc[:,0], Dataset_proc[:,1], s=dataPointSize, color=global_color, marker='.', linewidth=ln)
# The strange notation for the eigenvals is to match the methodology of `scale` option,
# since the larger it is, the shorter the vector.
plt.quiver(PCs[0,0], PCs[0,1], scale=40*(1-eigvals[0]), color=PCColour, width=0.014)
plt.quiver(PCs[1,0], PCs[1,1], scale=10*(1-eigvals[1]), color=PCColour, width=0.014)
plt.axis('equal')
plt.yticks([]), plt.xticks([])
plt.title('Globally applied PCA', **csfont, fontsize=font_text, color=PCColour)
plt.scatter(0, 0, color=PCColour, marker='x', lineWidth=data_point, s=20);

# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)






# Second subplot
figureSubplot = plt.subplot(gs[1])

# Data generation:
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


plt.axis('equal')

plt.scatter(X[idx==0,0], X[idx==0,1], s=dataPointSize, c=parula_1, marker='.')
plt.scatter(X[idx==1,0], X[idx==1,1], s=dataPointSize, c=parula_2, marker='.')

origin = [centroids[0][0]], [centroids[0][1]]
plt.quiver(*origin, PCs[0][0,0], PCs[0][0,1], scale=30*(1-eigvals[0][0]), color=PCColour, width=0.007)
origin = [centroids[0][0]], [centroids[0][1]]
plt.quiver(*origin, PCs[0][1,0], PCs[0][1,1], scale=15*(1-eigvals[0][1]), color=PCColour, width=0.007)
origin = [centroids[1][0]], [centroids[1][1]]
plt.quiver(*origin, PCs[1][0,0], PCs[1][0,1], scale=30*(1-eigvals[1][0]), color=PCColour, width=0.007)
origin = [centroids[1][0]], [centroids[1][1]]
plt.quiver(*origin, PCs[1][1,0], PCs[1][1,1], scale=15*(1-eigvals[1][1]), color=PCColour, width=0.007)
plt.title('Locally applied PCA', **csfont, fontsize=font_text, color=PCColour)
plt.yticks([]), plt.xticks([])

# Plot centroids
plt.scatter(centroids[:, 0], centroids[:, 1], color=PCColour, marker='x', lineWidth=data_point, s=20);

for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

# plt.subplots_adjust(wspace=0, hspace=0.4)
plt.savefig('global-vs-local-pca-subplot.png', dpi = 500, bbox_inches='tight')
plt.show()
