function [] = plot_eigenvalue_weights_bar_plot(A, n_mode_sets, n_request_eigvals, mode_name, annotations, labels, colors, destination)
%{
This function plots annotated bar plots from normalized eigenvalue weights.

INPUT PARAMETERS ----------------------------------------------------------

- A

    a matrix with eigenvalues.
    This matrix needs to be composed of vertically stacked sub-matrices:

      Eigval-1     Eigval-M
    [                       ] weight 1
    [                       ] weight 2
    [                       ]   .
    [       Mode set 1      ]   .
    [                       ]   .
    [                       ]   .
    [                       ] weight M
     -----------------------
    [                       ] weight 1
               ...

    Each such sub-matrix is associated with one label, marker and color.

    It is assumed that all mode sets have the same dimensions.

- n_mode_sets

    is an integer specifying the number of mode sets stacked into matrix A.

- n_request_eigvals

    is an integer specifying the number of first eigenvalues requested for plotting.

- mode_name

    is a string specifying the mode name.

    Example: mode_name = 'PC'

- annotations

    is a cell array of strings that annotates bars.

    Example: annotations = {'Bar-1', 'Bar-2', 'Bar-3', 'Bar-4'}

- labels

    is a cell array of strings that labels consecutive mode sets.

    Example: labels = {'Set-1', 'Set-2'}

- colors

    is a matrix of RGB vectors that specify colors for the consecutive
    mode sets bars.

    Example: colors = [
                      [ 0           0           0  ]
                      [	0.4660      0.6740      0.1880]
                      [	0           0.4470      0.7410]
                      [	0.8500      0.3250      0.0980]]
- destination

    is a string specifying the plot saving destination.

    Example: destination = 'PLOTS/'

%}

%% Checks:
[n_weights, n_eigvals] = size(A);

if mod(n_weights, n_mode_sets) ~= 0
    error(['The number of rows in A needs to be divisible by the number of mode sets.']);
end

n_weights = n_weights/n_mode_sets;

if ~exist('destination') || isempty(destination)
    destination = '';
end

%% Plotting parameters:
fontsize_axes = 18;
fontsize_label = 30;
fontsize_legend = 26;
text_size = 26;

%% Bar plot of a single eigenvalue:
for i=1:1:n_request_eigvals

    A_plot = [];

    % Extract single ith eigenvalue from each modes set:
    for mode_set = 1:1:n_mode_sets
        A_plot = [A_plot, A(((mode_set-1)*n_weights + 1):(mode_set*n_weights), i)];
    end

    % Bar plots:
    figure(i)
    set(gcf, 'Units', 'Normalized', 'OuterPosition', [0, 0, 0.8, 1]);
    b = bar(A_plot, 0.9);
    for int = 1:1:n_mode_sets
        b(int).EdgeColor = colors(int,:);
        b(int).FaceColor = colors(int,:);
    end

    % Annotate bars:
    for int = 1:1:n_weights

        x_pos = int;

        max_weight = max(A_plot(int,:));
        min_weight = min(A_plot(int,:));

        if max_weight > 0.7
            y_pos = -0.05;
            text(x_pos, y_pos, char(annotations(int)), 'FontSize', text_size, 'Rotation', 90, 'HorizontalAlignment', 'right');
        elseif min_weight < -0.7
            y_pos = 0.05
            text(x_pos, y_pos, char(annotations(int)), 'FontSize', text_size, 'Rotation', 90, 'HorizontalAlignment', 'left');
        elseif max_weight > 0
            y_pos = max_weight + 0.05;
            text(x_pos, y_pos, char(annotations(int)), 'FontSize', text_size, 'Rotation', 90, 'HorizontalAlignment', 'left');
        elseif min_weight < 0
            y_pos = 0.05;
            text(x_pos, y_pos, char(annotations(int)), 'FontSize', text_size, 'Rotation', 90, 'HorizontalAlignment', 'left');
        end

    end

    xticklabels([]);
    set(gca, 'FontSize', fontsize_axes)
    ylabel(['Weights on ', mode_name, '-', num2str(i), ' [-]'], 'FontSize', fontsize_label);
    ylim([-1 1])
    grid 'on'

    % Create legend from labels:
    l = cell(1, n_mode_sets);

    for int = 1:1:n_mode_sets
        l{int} = char(labels(int));
    end

    legend(b, l, 'Location', 'southeast', 'FontSize', fontsize_legend, 'Orientation', 'horizontal');

    % Save plot:
    filename = [destination, '_', mode_name, '_', num2str(i), '.eps'];
    saveas(gcf, filename, 'epsc');
    close all

end
