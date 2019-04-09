clc, clear, close all

%% GPR

% Training inputs:
x = [-1.5, -1.2, -0.5, 0.5, 1.5];

% Training targets:
y = sin(2*x);

% Reshape to columns for GPML:
x = x'; y = y';

% Points requested for the GPR prediction:
xs = linspace(-2, 2, 100)';             

% Mean function (none):
meanfunc = [];

% Squared Exponental covariance function:
covfunc = @covSEiso;              

% Gaussian likelihood:
likfunc = @likGauss;

% Tuning hyperparameters:
hyp = struct('mean', [], 'cov', [0 0], 'lik', -1);
hyp2 = minimize(hyp, @gp, -100, @infGaussLik, meanfunc, covfunc, likfunc, x, y);

% Performing GPR:
[mu s2] = gp(hyp2, @infGaussLik, meanfunc, covfunc, likfunc, x, y, xs);

%% Plotting

% Plotting parameters:
fontsize_axes = 22;
fontsize_label = 40;
fontsize_legend = 40;

set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0, 0.8, 1]);
hold on, grid on, box on
set(gca, 'FontSize', fontsize_axes)

% Plot uncertainty:
f = [mu + 2 * sqrt(s2); flipdim(mu - 2 * sqrt(s2), 1)];
fill([xs; flipdim(xs,1)], f, [7 7 7]/8)

% Plot GPR reconstruction:
plot(xs, mu, 'r--', 'LineWidth', 2)

% Plot training data points:
plot(x, y, 'ok', 'LineWidth', 2, 'MarkerFaceColor', 'k')

xlabel(['x'], 'FontSize', fontsize_label); ylabel(['y'], 'FontSize', fontsize_label);

% Save plot:
filename = ['GPR-GPML.eps'];
saveas(gcf, filename, 'epsc');
close all
