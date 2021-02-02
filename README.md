# matplotlib-templates
Some templates for experimental plots.

## Enviornment

python 3.7

### Using default colors of a style

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

default_colors = []
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    default_colors.append(color["color"])
    print(color["color"], type(color["color"]))

print(default_colors[0], type(default_colors[0]))

""" e.g.
rects_CPU_47  = ax0.bar(x - width/2, latency_CPU_total_47, width, color=default_colors[0])
"""
```

<img src="images/default_colors_fivethirtyeight.png" alt="default_colors_fivethirtyeight" style="zoom:50%;" />

<img src="images/default_colors_ggplot.png" alt="default_colors_ggplot" style="zoom:50%;" />

<img src="images/default_colors_grayscale.png" alt="default_colors_grayscale" style="zoom:50%;" />

<img src="images/default_colors_seaborn-deep.png" alt="default_colors_seaborn-deep" style="zoom:50%;" />

<img src="images/default_colors_seaborn-pastel.png" alt="default_colors_seaborn-pastel" style="zoom:50%;" />

<img src="images/default_colors_seaborn.png" alt="default_colors_seaborn" style="zoom:50%;" />

## bar_and_plot

![bar_and_plot](images/bar_and_plot.png)


## plot

3 variables: x, y, curve

![plot](images/plot.png)


## plot_fill

3 variables: x, y, curve

![plot](images/plot_fill.png)

## bar_horizontal

![bar_horizontal](images/bar_horizontal.png)


## bar_horizontal_percentage

![bar_horizontal_percentage](images/bar_horizontal_percentage.png)

## grouped_bar

![grouped_bar](images/grouped_bar.png)

## stacked_grouped_bar

![grouped_bar](images/stacked_grouped_bar.png)
