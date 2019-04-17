# PCA in Matlab

## TL;DR

For a pre-processed `DATA` (centered and scaled):

```Matlab
[PCs, PC_scores, eigenvalues, tsquared, variance_explained, mu] = pca(DATA, 'Centered', false);
```
