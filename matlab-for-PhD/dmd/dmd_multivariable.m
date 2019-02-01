function [data_dmd, lambda] = dmd_multivariable(data_set, r, dt)

%{
Performs exact DMD on a multivariable, time-resolved data set D.

- data_set

    data set D of size (space x time).

- r

    SVD rank approximation.

- dt

    time step.

Returns the rank-r approximation of the data set and the eigenvalues.
%}

%% Past and future state split:
X1 = data_set(:, 1:end-1);
X2 = data_set(:, 2:end);

%% Perform DMD approximation of rank r:
% SVD:
[U, Sigma, V] = svd(X1, 'econ');

% Rank-r truncation:
U_r = U(:,1:1:r);
Sigma_r = Sigma(1:r, 1:r);
V_r = V(:, 1:1:r);

% Linear propagator:
Aprop = U_r' * X2 * V_r * inv(Sigma_r);

% Eigendemposition:
[W, Lam] = eig(Aprop);

% DMD modes:
Phi = X2 * V_r * inv(Sigma_r) * W;

% Initial condition:
x1 = X1(:,1);
b = Phi\x1;

% Time dynamics:
nt = size(data_set, 2);
time  = zeros(r, nt);
lambda = diag(Lam);
omega = log(lambda)/dt;

for iter=1:1:nt
    time(:,iter) = b.*exp(omega*iter*dt);
end

%% Data approximation, real part:
data_dmd = real(Phi*time);