# Matlab for PhD - quick cheatsheet

## Set default LaTeX interpreters

```
set(groot, 'DefaultTextInterpreter', 'LaTex');
set(groot, 'DefaultLegendInterpreter', 'LaTex');
set(groot, 'DefaultAxesTickLabelInterpreter', 'LaTex');
```

`groot` - root graphics object

## Scatter plot

```
scatter(x, y, 20, 'k+', 'LineWidth', 2)
```

`x, y` - data

`20` - marker size

`'k+''` - marker colour and style

`'LineWidth', 2` - marker line width

## Font size adjusting

`set(gca,'FontSize', 14);` - font size of axis ticks

`xlabel(['x'], 'FontSize', 14)` - font size for x-axis xlabel

`ylabel(['y'], 'FontSize', 14)` - font size for y-axis xlabel

`title(['Graph $\omega(x)$'], 'FontSize', 14)` - font size for title
