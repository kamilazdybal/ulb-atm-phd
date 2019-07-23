function [X_tilde, centers, scales] = center_and_scale(X, cent_crit, scal_crit)
%{
This function centers and scales raw data.

Inputs: ---

    - X

        unscaled and uncetered (raw) data set.

    - cent_crit

        centering criteria selected.

        Centerings:     Subtracted from each variable:

        - 'none'        (0)
        - 'mean'        (mean)
        - 'min'         (min)

    - scal_crit

        scaling criteria selected.

        Scalings:       Each variable is divided by:

        - 'none'        (1)
        - 'auto'        (standard deviation)
        - 'range'       (max - min)
        - 'pareto'      (square root of standard deviation)
        - 'vast'        (standard deviation squared divided by mean)
        - 'level'       (mean)
        - 'max'         (max)
        - 'stdrange'    (standard deviation divided by (max - min))
        - 'stdmax'      (standard deviation divided by max)

Outputs: ---

    - X_tilde

        scaled and centered data set.

    - centers

        array with centers that were subtracted from the raw data set. To
        be used for uncentering.

    - scales

        array with scales with which the raw data set was divided by. To be
        used for unscaling.

%}

%% Tolerance to avoid dividing by zero:
a_tol = 1e-16;

cent_crit = lower(cent_crit);
scal_crit = lower(scal_crit);

%% Centering options:
switch cent_crit
    case {'none'}
        centers = zeros(size(X));
    case {'mean'}
        centers = mean(X);
    case {'min'}
        centers = min(X);
    otherwise
        error('Unknown centering criterion.');
end

%% Scaling options:
switch scal_crit
    case 'none'
        scales = ones(size(X));
    case 'auto'
        scales = std(X);
    case 'range'
        scales = max(X) - min(X);
    case 'pareto'
        scales = sqrt(std(X));
    case 'vast'
        scales = std(X).^2 ./ (mean(X) + a_tol);
    case 'level'
        scales = mean(X);
    case 'max'
        scales = max(X);
    case 'stdrange'
        scales = std(X) ./ (max(X) - min(X) + a_tol);
    case 'stdmax'
        scales = std(X) ./ (max(X) + a_tol);
    otherwise
        error('Unknown scaling criterion.');
end

%% Centering and scaling data set:
X_tilde = (X - centers) ./ (scales + a_tol);
