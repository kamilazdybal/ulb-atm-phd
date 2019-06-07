def varimax(A, gamma = 1.0, q = 20, tol = 1e-6):
"""
Varimax rotation performs an orthogonal rotation of factors that maximizes the sum of the variances of the squared loadings.

A           matrix of factors stored in columns
gamma
q           number of iterations
tol         tolerance

"""
    from scipy import eye, asarray, dot, sum, svd
    import numpy as np

    p,k = A.shape
    R = eye(k)
    d = 0

    for i in xrange(q):
        d_old = d
        Lambda = dot(A, R)
        u,s,vh = svd(dot(A.T,asarray(Lambda)**3 - (gamma/p) * dot(Lambda, diag(diag(dot(Lambda.T,Lambda))))))
        R = dot(u,vh)
        d = sum(s)
        if d_old!=0 and d/d_old < 1 + tol: break

    return dot(A, R)
