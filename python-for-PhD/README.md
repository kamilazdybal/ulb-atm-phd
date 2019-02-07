# Python for PhD

> You will be grateful tomorrow for the automation you do today.

This is a repository of Python tool-codes to boost your everyday PhD life.

## Installing Charter font for `matplotlib`

I am not sure which of these made it work.

Download font here:

https://practicaltypography.com/charter.html

Place `.ttf` files in the location which matplotlib uses (I also placed it in system font location, just in case). Change names to replace spaces with "-", e.g.

`Charter-Bold.ttf`

In your Python console, rebuild:

```python
import matplotlib.font_manager
matplotlib.font_manager._rebuild()
```

Refer to Charter font wherever needed:

```python
charter_regular_font = {'fontname':'Charter', 'fontweight':'regular'}
charter_bold_font = {'fontname':'Charter', 'fontweight':'bold'}
```

Happy LaTeXing!

## Issue: figure background color not preserved when saving the figure

Solution:

```python
background_col = "#E6FFCC"
figureSubplot.set_facecolor(background_col)
plt.rcParams['savefig.facecolor'] = background_col
```
