# PCA example on a 2D, randomized linear data set
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

# Styles:
lineColour = '#f44242'
PCColour = '#002f72'
scoresColour = '#ff7d14'
ln = 1

# Fonts:
csfont = {'fontname':'cmr10'}
hfont = {'fontname':'cmr10'}

# Generate randomized dataset with linearity
Np = 100
Nq = 2
x = np.linspace(3, 6, Np)
y = 0.8*x + 1*np.random.rand(Np)
Dataset = np.column_stack((x, y))
Dataset_proc = Dataset - np.mean(Dataset, axis=0)

# Perform PCA
pca = PCA(n_components=Nq)
pca.fit(Dataset)
scores = pca.transform(Dataset)
PCs = pca.components_
eigvals = pca.explained_variance_ratio_

Dataset_projected = np.dot(Dataset_proc, np.transpose(np.mat(PCs[0,:])))
Dataset_approx = np.dot(np.transpose(np.mat(scores[:,0])), np.mat(PCs[0,:])) + np.mean(Dataset, axis=0)

# Plot PCA steps
figure = plt.figure(figsize=(11, 8))
plt.subplot(2,3,1)
plt.scatter(Dataset[:,0], Dataset[:,1], color=lineColour, marker='.', linewidth=ln)
plt.title('Raw dataset', **csfont)
plt.axis('equal')
plt.yticks([3, 4, 5, 6]), plt.xticks([3, 4, 5, 6])

plt.subplot(2,3,2)
plt.scatter(Dataset_proc[:,0], Dataset_proc[:,1], color=lineColour, marker='.', linewidth=ln)
plt.title('Raw dataset centered', **csfont)
plt.axis('equal')
plt.yticks([-1, 0, 1]), plt.xticks([-1, 0, 1])

plt.subplot(2,3,3)
plt.scatter(Dataset_proc[:,0], Dataset_proc[:,1], color=lineColour, marker='.', linewidth=ln)
# The strange notation for the eigenvals is to match the methodology of `scale` option,
# since the larger it is, the shorter the vector.
plt.quiver(PCs[0,0], PCs[0,1], scale=70*(1-eigvals[0]), color=PCColour, width=0.01)
plt.quiver(PCs[1,0], PCs[1,1], scale=10*(1-eigvals[1]), color=PCColour, width=0.01)
plt.title('Principal components', **csfont)
plt.axis('equal')
plt.yticks([-1, 0, 1]), plt.xticks([-1, 0, 1])

plt.subplot(2,3,4)
plt.scatter(scores[:,0], scores[:,1], color=scoresColour, marker='.', linewidth=ln)
plt.title('PC-scores', **csfont)
plt.axis('equal')
plt.yticks([-2, 0, 2]), plt.xticks([-2, 0, 2])

plt.subplot(2,3,5)
plt.scatter([Dataset_projected], [np.mat(np.zeros(Np))], color=scoresColour, marker='.', linewidth=ln)
plt.title('Data projection', **csfont)
plt.axis('equal')
plt.yticks([0]), plt.xticks([-2, 0, 2])

plt.subplot(2,3,6)
plt.scatter([Dataset_approx[:,0]], [Dataset_approx[:,1]], color=lineColour, marker='.', linewidth=ln)
plt.title('Data approximation', **csfont)
plt.axis('equal')
plt.yticks([3, 4, 5, 6]), plt.xticks([3, 4, 5, 6])

# Save plot:
filename = 'DWGs/PCA-example-subplot.png'
plt.savefig(filename, dpi = 500)
plt.show()
plt.close()
