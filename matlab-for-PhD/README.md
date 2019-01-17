# Matlab for PhD - quick cheatsheet

## Set default LaTeX interpreters

```matlab
set(groot, 'DefaultTextInterpreter', 'LaTex');
set(groot, 'DefaultLegendInterpreter', 'LaTex');
set(groot, 'DefaultAxesTickLabelInterpreter', 'LaTex');
```

`groot` - root graphics object

## Scatter

```matlab
scatter(x, y, 20, 'k+', 'LineWidth', 2)
```

`x, y` - data

`20` - marker size

`'k+'` - marker colour and style

`'LineWidth', 2` - marker line width

## Plotting in a loop

```matlab
plotmarkers = {'-o', '-s', '-d', '-^', '-p', '->', '-*', '-+'};

colors = [
[         0         0         0] % black
[         0    0.4470    0.7410] % blue
[    0.8500    0.3250    0.0980] % red
[    0.4940    0.1840    0.5560] % purple
[    0.9290    0.6940    0.1250] % yellow
[    0.4660    0.6740    0.1880] % green
[    0.3010    0.7450    0.9330]
[    0.6350    0.0780    0.1840]];

for iter 1:1:length(plotmarkers)

  p = plot(variable(iter), char(plotmarkers(iter))), hold on, grid 'on'
  set(gca,'YScale','log');
  p.Color = colors(iter,:);
  p.MarkerSize = 8;
  p.MarkerFaceColor = colors(iter),:);
  p.LineWidth = 0.5;

end
```

## Font size adjusting

```matlab
set(gca,'FontSize', 14); % font size of axis ticks
xlabel(['x'], 'FontSize', 14); % font size for x-axis xlabel
ylabel(['y'], 'FontSize', 14); % font size for y-axis xlabel
title(['Graph $y(x)$'], 'FontSize', 14); % font size for title
```
