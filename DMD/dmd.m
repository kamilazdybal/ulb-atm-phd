clear all, close all, clc

% x-domain:
xi = linspace(-10, 10, 400);

% time domain:
t = linspace(0,4*pi, 200);

% Evenly spaced in time:
dt = t(2)-t(1);

[Xgrid, T] = meshgrid(xi, t);

% Create two spatial-temporal patterns:
f1 = sech(Xgrid + 3).*(1*exp(i*2.3*T));
f2 = (sech(Xgrid).*tanh(Xgrid)).*(2*exp(i*2.8*T));
f = f1+f2;
[u, s, v] = svd(f.');


figure(2)
plot(diag(s)/sum(diag(s)), 'ro')

figure(3)
subplot(2,1,1), plot(real(u(:,1:2)))
subplot(2,1,2), plot(real(v(:,1:2)))

%% DMD
X = f.';

X1 = X(:,1:end-1);
X2 = X(:,2:end);

% Rank truncation:
r = 2;
[U, S, V] = svd(X1, 'econ');

Ur = U(:,1:r);
Sr = S(1:r, 1:r);
Vr = V(:, 1:r);

Atilde = Ur'*X2*Vr/Sr;
[W,D] = eig(Atilde);
Phi = X2 * Vr/Sr*W; % DMD modes

lambda = diag(D);
omega = log(lambda)/dt;

figure(3)
subplot(2,1,1), hold on, plot(real(Phi), 'Linewidth', [2])

% Reconstruction in time:
x1 = X(:,1);
b = Phi\x1;
time_dynamics = zeros(r, length(t));

for iter=1:length(t)
  time_dynamics(:, iter) = (b.*exp(omega*t(iter)));

end

X_dmd = Phi*time_dynamics;

figure(1)
subplot(2,2,1), surfl(Xgrid, T, real(f1)); shading interp, colormap(gray)
subplot(2,2,2), surfl(Xgrid, T, real(f2)); shading interp, colormap(gray)
subplot(2,2,3), surfl(Xgrid, T, real(f)); shading interp, colormap(gray)
subplot(2,2,4), surfl(Xgrid, T, real(X_dmd).'); shading interp, colormap(gray)


pause(10)

% awesomeness
