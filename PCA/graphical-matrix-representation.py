import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

# Styles:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
lineColour = '#f44242'
PCColour = '#002f72'
scoresColour = '#ff7d14'
randomColour = '#dee9fc'
semiColour = '#94b7ef'
structuredColour = '#3178ea'
ln = 2
fnts = 16
plt.rc('grid', linestyle="--", color='black', linewidth=0.1)

# Fonts:
csfont = {'fontname':'Charter', 'fontweight':'regular'}
hfont = {'fontname':'Charter', 'fontweight':'bold'}
font_axis = 10

# Generate random data set: ====================================================
Dataset_random = np.random.rand(10,6)
Dataset_random = Dataset_random/np.max(Dataset_random)
mu = np.mean(Dataset_random, axis=0)

# Perform PCA:
pca = PCA()
pca.fit(Dataset_random)
scores = pca.transform(Dataset_random)
PCs = pca.components_
eigvals_random = pca.explained_variance_ratio_

# Display original matrix:
figure = plt.figure(figsize=(4, 5))
figureSubplot = figure.add_subplot(1,1,1)
plt.imshow(Dataset_random, vmin=0, vmax=1)
plt.yticks([]), plt.xticks([])
figureSubplot.spines["top"].set_visible(False)
figureSubplot.spines["bottom"].set_visible(False)
figureSubplot.spines["right"].set_visible(False)
figureSubplot.spines["left"].set_visible(False)

# Annotate the imshow:
for i in range(10):
    for j in range(6):
        text = plt.text(j, i, round(Dataset_random[i, j], 1),
                       ha="center", va="center", color="w")

# Save plot:
filename = 'DWGs/random-matrix-original.png'
plt.savefig(filename, dpi = 100, bbox_inches='tight')
plt.close()

# PCs bar plot:
for pc in range(1,7):
    figure = plt.figure(figsize=(4, 3))
    figureSubplot = figure.add_subplot(1,1,1)
    plt.grid()
    plt.bar(range(1,7), pca.components_[pc-1,:], 0.5)

    # Save plot:
    filename = 'DWGs/random-matrix-bar-plot-PC' + str(pc) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

for Nq in range(1,7):

    Dataset_approx = np.dot(pca.transform(Dataset_random)[:,:Nq], pca.components_[:Nq,:])
    Dataset_approx += mu

    figure = plt.figure(figsize=(6.3, 10))

    figureSubplot = plt.subplot(2,2,2)
    plt.imshow(pca.components_[:Nq,:], vmin=-1, vmax=1)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,3)
    plt.imshow(pca.transform(Dataset_random)[:,:Nq])
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,4)
    plt.imshow(Dataset_approx)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)
    plt.subplots_adjust(wspace=0.1, hspace=0)

    # Annotate the imshow:
    for i in range(10):
        for j in range(6):
            text = plt.text(j, i, round(Dataset_approx[i, j], 1),
                           ha="center", va="center", color="w")

    # Save plot:
    filename = 'DWGs/random-matrix-reconstruction-PCs-' + str(Nq) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

# Generate semi-structured data set: ===========================================
Dataset_semi_structured = np.array([[2, 3, 1, 0, 4, 5],
                    [3, 4, 2, 10, 12, 5],
                    [2, 6, 7, 10, 10, 9],
                    [5, 7, 12, 11, 8, 9],
                    [1, 9, 4, 5, 12, 7],
                    [1, 6, 3, 8, 3, 9],
                    [3, 7, 5, 8, 0, 4],
                    [0, 1, 7, 7, 1, 8],
                    [0, 1, 1, 3, 6, 11],
                    [2, 2, 1, 7, 7, 10]])

Dataset_semi_structured = Dataset_semi_structured/np.max(Dataset_semi_structured)
mu = np.mean(Dataset_semi_structured, axis=0)

# Perform PCA:
pca = PCA()
pca.fit(Dataset_semi_structured)
scores = pca.transform(Dataset_semi_structured)
PCs = pca.components_
eigvals_semi_structured = pca.explained_variance_ratio_

# Display matrix:
figure = plt.figure(figsize=(4, 5))
figureSubplot = plt.subplot(1,1,1)
plt.imshow(Dataset_semi_structured, vmin=0, vmax=1)
plt.yticks([]), plt.xticks([])
#plt.colorbar()
figureSubplot.spines["top"].set_visible(False)
figureSubplot.spines["bottom"].set_visible(False)
figureSubplot.spines["right"].set_visible(False)
figureSubplot.spines["left"].set_visible(False)

# Annotate the imshow:
for i in range(10):
    for j in range(6):
        text = plt.text(j, i, round(Dataset_semi_structured[i, j], 1),
                       ha="center", va="center", color="w")

# Save plot:
filename = 'DWGs/semi-structured-matrix-original.png'
plt.savefig(filename, dpi = 100, bbox_inches='tight')
plt.close()

# PCs bar plot:
for pc in range(1,7):
    figure = plt.figure(figsize=(4, 3))
    figureSubplot = figure.add_subplot(1,1,1)
    plt.grid()
    plt.bar(range(1,7), pca.components_[pc-1,:], 0.5)

    # Save plot:
    filename = 'DWGs/semi-structured-matrix-bar-plot-PC' + str(pc) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

for Nq in range(1,7):

    Dataset_approx = np.dot(pca.transform(Dataset_semi_structured)[:,:Nq], pca.components_[:Nq,:])
    Dataset_approx += mu

    figure = plt.figure(figsize=(6.3, 10))

    figureSubplot = plt.subplot(2,2,2)
    plt.imshow(pca.components_[:Nq,:], vmin=-1, vmax=1)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,3)
    plt.imshow(pca.transform(Dataset_semi_structured)[:,:Nq])
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,4)
    plt.imshow(Dataset_approx)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)
    plt.subplots_adjust(wspace=0.1, hspace=0)

    # Annotate the imshow:
    for i in range(10):
        for j in range(6):
            text = plt.text(j, i, round(Dataset_approx[i, j], 1),
                           ha="center", va="center", color="w")

    # Save plot:
    filename = 'DWGs/semi-structured-matrix-reconstruction-PCs-' + str(Nq) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

# Generate structured data set: ================================================
Dataset_structured = np.array([[2, 2, 5, 4, 4, 5],
                    [3, 4, 3, 10, 12, 10],
                    [2, 6, 7, 10, 10, 9],
                    [5, 7, 12, 11, 10, 12],
                    [1, 5, 4, 5, 12, 9],
                    [1, 6, 3, 6, 7, 8],
                    [2, 3, 5, 6, 6, 7],
                    [0, 1, 5, 6, 2, 3],
                    [0, 1, 1, 3, 3, 2],
                    [1, 2, 1, 2, 2, 1]])

Dataset_structured = Dataset_structured/np.max(Dataset_structured)
mu = np.mean(Dataset_structured, axis=0)
# Perform PCA
pca = PCA()
pca.fit(Dataset_structured)
scores = pca.transform(Dataset_structured)
PCs = pca.components_
eigvals_structured = pca.explained_variance_ratio_

# Display matrix:
figure = plt.figure(figsize=(4, 5))
figureSubplot = plt.subplot(1,1,1)
plt.imshow(Dataset_structured, vmin=0, vmax=1)
plt.yticks([]), plt.xticks([])
#plt.colorbar()
figureSubplot.spines["top"].set_visible(False)
figureSubplot.spines["bottom"].set_visible(False)
figureSubplot.spines["right"].set_visible(False)
figureSubplot.spines["left"].set_visible(False)

# Annotate the imshow:
for i in range(10):
    for j in range(6):
        text = plt.text(j, i, round(Dataset_structured[i, j], 1),
                       ha="center", va="center", color="w")

# Save plot:
filename = 'DWGs/structured-matrix-original.png'
plt.savefig(filename, dpi = 500, bbox_inches='tight')
plt.close()

# PCs bar plot:
for pc in range(1,7):
    figure = plt.figure(figsize=(4, 3))
    figureSubplot = figure.add_subplot(1,1,1)
    plt.grid()
    plt.bar(range(1,7), pca.components_[pc-1,:], 0.5)

    # Save plot:
    filename = 'DWGs/structured-matrix-bar-plot-PC' + str(pc) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

for Nq in range(1,7):

    Dataset_approx = np.dot(pca.transform(Dataset_structured)[:,:Nq], pca.components_[:Nq,:])
    Dataset_approx += mu

    figure = plt.figure(figsize=(6.3, 10))

    figureSubplot = plt.subplot(2,2,2)
    plt.imshow(pca.components_[:Nq,:], vmin=-1, vmax=1)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,3)
    plt.imshow(pca.transform(Dataset_structured)[:,:Nq])
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)

    figureSubplot = plt.subplot(2,2,4)
    art = plt.imshow(Dataset_approx)
    plt.yticks([]), plt.xticks([])
    figureSubplot.spines["top"].set_visible(False)
    figureSubplot.spines["bottom"].set_visible(False)
    figureSubplot.spines["right"].set_visible(False)
    figureSubplot.spines["left"].set_visible(False)
    plt.subplots_adjust(wspace=0.1, hspace=0)

    # Annotate the imshow:
    for i in range(10):
        for j in range(6):
            text = plt.text(j, i, round(Dataset_approx[i, j], 1),
                           ha="center", va="center", color="w")

    # Save plot:
    filename = 'DWGs/structured-matrix-reconstruction-PCs-' + str(Nq) + '.png'
    plt.savefig(filename, dpi = 100, bbox_inches='tight')
    plt.close()

# Save eigenvalues comparison: =================================================
figure = plt.figure(figsize=(5, 3))
figureSubplot = plt.subplot(1,1,1)
p1, = plt.plot(range(1,7), eigvals_random, 'o-', color=randomColour, linewidth=ln)
p2, = plt.plot(range(1,7), eigvals_semi_structured, 'o-', color=semiColour, linewidth=ln)
p3, = plt.plot(range(1,7), eigvals_structured, 'o-', color=structuredColour, linewidth=ln)
L = figureSubplot.legend((p1, p2, p3), ('Random', 'Semi-structured', 'Structured'))
plt.setp(L.texts, family='Charter')

# Set the tick labels font
for label in (figureSubplot.get_xticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

for label in (figureSubplot.get_yticklabels()):
    label.set_fontname('Charter')
    label.set_fontweight('regular')
    label.set_fontsize(font_axis)

filename = 'DWGs/matrix-reconstruction-eigenvalues-comparison.png'
plt.savefig(filename, dpi = 500, bbox_inches='tight')
plt.close()
