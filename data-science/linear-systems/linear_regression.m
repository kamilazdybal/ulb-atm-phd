%% Partial Least Squares regression (PLS)
clc, clear, close all

fontsize_axes = 18;
point_colour = [128,141,160]./256;
regression_colour = [38,138,198]./256;

%% Generate 2D data set:
mu = [2 2];
sigma = [1 1.5; 1.5 3];
rng('default');
R = mvnrnd(mu,sigma,200);
Y = R(:,2);

%% LS with linear basis functions:
X = [R(:,1), ones(size(R(:,1)))];

% Find the PLS regression:
Y_tilde = X*inv(X'*X)*X'*Y;

% Plot:
figure;
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0, 0.4, 0.5]);
scatter(R(:,1), Y, 40, point_colour, '.'); axis equal; hold on
plot(R(:,1), Y_tilde, 'k-', 'color', regression_colour, 'LineWidth', 2);
set(gca, 'FontSize', fontsize_axes)
box on
saveas(gcf, 'LS-linear-basis-functions.eps', 'epsc');

%% LS with nonlinear (quadratic) basis functions:
X = [R(:,1).^2, R(:,1), ones(size(R(:,1)))];

% Find the PLS regression:
Y_tilde = X*inv(X'*X)*X'*Y;

% Plot:
figure;
set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0, 0.4, 0.5]);
scatter(R(:,1), Y, 40, point_colour, '.'); axis equal; hold on
scatter(R(:,1), Y_tilde, 60, regression_colour, '.');
set(gca, 'FontSize', fontsize_axes)
box on
saveas(gcf, 'LS-nonlinear-basis-functions.eps', 'epsc');




close all
