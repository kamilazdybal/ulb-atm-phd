function [X] = uncenter_and_unscale(X_tilde, centers, scales)
%{
This function uncenters and unscales data.

Inputs: ---

    - X_tilde

        scaled and cetered data set.

    - centers

        array with centers that were subtracted from the raw data set. To
        be used for uncentering.

    - scales

        array with scales with which the raw data set was divided by. To be
        used for unscaling.

Outputs: ---

    - X

        unscaled and uncentered (raw) data set.

%}

%% Uncentering and unscaling data set:
X = X_tilde .* scales + centers;
