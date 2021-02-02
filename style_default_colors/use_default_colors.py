import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def get_default_colors():

  default_colors = []
  for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
      default_colors.append(color["color"])
      print(color["color"], type(color["color"]))

  return default_colors

# print(default_colors[0], type(default_colors[0]))


def add_colored_bars(ax, default_colors):
    l = len(default_colors)
    x = np.arange(l)
    y = [1] * l
    for i in range(l):
        ax.bar(i, 1, color=default_colors[i])

styles = ['ggplot', 'fivethirtyeight', 'seaborn', 'seaborn-deep', 'seaborn-pastel', 'grayscale']

for style in styles:
    plt.style.use(style)
    fig, ax = plt.subplots(1, 1)
    default_colors = get_default_colors()
    add_colored_bars(ax, default_colors)
    ax.set_title("Default colors: {}".format(style))

    plt.savefig('../images/default_colors_{}.png'.format(style, transparent=False, dpi=200, bbox_inches="tight"))