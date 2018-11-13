n = 4
X = [1,2,3,1 ; 2, 3, 10, 0 ; 0, 1,1,1 ; 4, 2, 2, 10];

X1 = X(:,1:n-1)
X2 = X(:,2:n)

% Solve system X2 = A X1:
X1_pinv = pinv(X1)
A = X2 * X1_pinv;
X1 * X1_pinv
X1_pinv * X1
A*X1
