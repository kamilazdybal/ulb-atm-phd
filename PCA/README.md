# Notes on Principal Component Analysis

## PCA in Matlab

```Matlab
% PCA of a data set X:

[PCs, PC_scores, eigenvalues, tsquared, variance_explained, mu] = pca(X)
```

## PCA in Python

```Python
# PCA of a data set X:
pca = PCA()
pca.fit(X)
PC_scores = pca.transform(X)
PCs = pca.components_
eigenvalues = pca.explained_variance_ratio_
```

## PCA in pictures

![Screenshot](DWGs/PCA-example-subplot.png)
