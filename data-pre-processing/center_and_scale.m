function [X_tilde, centers, scales] = center_and_scale(X, cent_crit, scal_crit)
%{
This function centers and scales raw data.

Inputs: ---

    - X

        unscaled and uncetered (raw) data set.

    - cent_crit

        centering criteria selected.

        Available centerings:

            - 'none'
            - 'mean'    (mean)
            - 'min'     (min)

    - scal_crit

        scaling criteria selected.

        Available scalings:

            - 'none'
            - 'auto'    (standard deviation)
            - 'range'   (max - min)
            - 'pareto'  (square root of standard deviation)
            - 'vast'    (standard deviation times standard deviation divided by mean)
            - 'level'   (mean)
            - 'max'     (max)

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

% Tolerance to avoid dividing by zero:
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
    otherwise
        error('Unknown scaling criterion.');
end

%% Centering and scaling data set:
X_tilde = (X - centers) ./ (scales + a_tol);
