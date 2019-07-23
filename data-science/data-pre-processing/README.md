# Data pre-processing

This repository contains codes for pre-processing raw data sets.

## Centering and scaling: example usage

```matlab
% Centering and scaling:
[X_tilde, centers, scales] = center_and_scale(raw_data, 'mean', 'auto');

% PCA:
[PCs, PC_scores] = pca(X_tilde, 'Centered', false);

% Data approximation:
X_app = PC_scores * PCs';

% Uncentering and unscaling:
[X] = uncenter_and_unscale(X_app, centers, scales);
```
