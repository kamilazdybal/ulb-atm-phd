# Local PCA
import numpy as np
from sklearn.decomposition import PCA

def local_pca(X, idx):
    """
    This function performs PCA in local clusters.

    The input should be pre-processed data set X.

    The LPCA function centers the observations in every cluster.
    """

    n_k = len(np.unique(idx))

    # Initialize the outputs:
    PCs = []
    eigvals = []
    PC_scores = []

    for k in range(0, n_k):

        # Extract local cluster:
        X_k = X[idx==k]

        # Possible data-set pre-processing in local cluster:
        #X_k = cas.mean_center(X_k)

        # Perform PCA in local cluster:
        pca = PCA()
        pca.fit(X_k)
        PC_scores.append(pca.transform(X_k))
        PCs.append(pca.components_)
        eigvals.append(pca.explained_variance_ratio_)

    return (PCs, eigvals, PC_scores)

def recover_from_lpca():
    pass
