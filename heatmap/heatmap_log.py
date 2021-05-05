



import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import seaborn
import numpy as np

print(matplotlib.__version__)

# Heatmap Document: https://seaborn.pydata.org/generated/seaborn.heatmap.html

fig, ax = plt.subplots()
# fig, ax = plt.subplots(figsize=(4, 4))

data_linear = np.random.randn(8,8)
data = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        data[i,j] = 10 ** data_linear[i,j]

print(data_linear)
print(np.min(data), np.max(data))

# matplotlib color map objects: https://matplotlib.org/stable/tutorials/colors/colormaps.html

cmap = 'RdBu'
# cmap = 'RdYlGn'
# cmap = 'coolwarm'
# cmap = 'bwr'
# cmap = 'seismic'

# matplotlib color map objects: https://matplotlib.org/stable/tutorials/colors/colormaps.html
# norm is an argument of matplotlib.axes.Axes.pcolormesh: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html
lognorm = LogNorm(vmin=np.min(data), vmax=np.max(data))
# print(lognorm)
ax_heatmap = seaborn.heatmap(data, norm=lognorm, cmap=cmap, cbar_kws={'label': 'colorbar title'})
# set colorbar label size by hacking: https://stackoverflow.com/questions/48586738/seaborn-heatmap-colorbar-label-font-size
# ax_heatmap.figure.axes[-1].yaxis.label.set_size(12)
ax_heatmap.figure.axes[-1].set_ylabel('colorbar title', fontsize=14, labelpad=10)
# ax_heatmap.figure.axes[-1].set_yticks([1e-3, 1e-2, 1e-1, 1, 1e+1, 1e+2, 1e+3])  
# ax_heatmap.figure.axes[-1].set_yticklabels([1e-3, 1e-2, 1e-1, 1, 1e+1, 1e+2, 1e+3])  # horizontal colorbar
# ax_heatmap.figure.axes[-1].locator_params(nbins=7)
# ax_heatmap.figure.axes[-1].get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatter(base=2, labelOnlyBase = False))
# ax_heatmap.figure.axes[-1].get_yaxis().set_major_formatter(matplotlib.ticker.LogFormatterSciNotation(base=10))


x_tick_labels = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7]
y_tick_labels = [2**10, 2**11, 2**12, 2**13, 2**14, 2**15, 2**16, 2**17]
# 2**10 is on the very top in the heatmap, we want to put it down
##### Note: here can cause bug, reverse data also! ######s
y_tick_labels.reverse()
# for i in range(len(x_tick_labels)):
#     x_tick_labels[i] = str(x_tick_labels[i])
# for i in range(len(y_tick_labels)):
#     y_tick_labels[i] = str(y_tick_labels[i])


ax.set_xticklabels(x_tick_labels)
ax.set_yticklabels(y_tick_labels)
plt.yticks(rotation=0)
# ax.ticklabel_format(axis='both', style='sci')
# ax.set_yscale("log")

ax.tick_params(length=0, top=False, bottom=False, left=False, right=False, 
    labelleft=True, labelbottom=True, labelsize=12)
ax.set_xlabel('ax_xlabel', fontsize=16, labelpad=10)
ax.set_ylabel('ax_ylabel', fontsize=16, labelpad=10)
# ax.set_title('Linear Heatmap', fontsize=16, y=5)
plt.text(2, len(y_tick_labels) + 2, "Linear Heatmap", fontsize=16)

plt.savefig('../images/heatmap_log_{}.png'.format(cmap), transparent=False, dpi=200, bbox_inches="tight")

plt.show()