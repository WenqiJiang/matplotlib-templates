import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter
import pandas as pd
import seaborn as sns 

# Seaborn version >= 0.11.0

sns.set_theme(style="whitegrid")
# Set the palette to the "pastel" default palette:
# sns.set_palette("pastel")

### Note: For violin graph, a single violin's data must be in the same column
###   e.g., given 3 violin plots, each with 100 points, the shape of the array
###   should be (100, 3), where the first column is for the first violin and so forth
# fake up some data

num_category = 10

data = []
for i in range(num_category):
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    partial_data = np.concatenate((spread, center, flier_high, flier_low))
    data.append(partial_data)

reshaped_data = np.zeros((data[0].shape[0], num_category))

for i in range(num_category):
    reshaped_data[:, i] = data[i]

data = reshaped_data
print(data.shape)

plt.figure(figsize=(12, 3))
# API: https://seaborn.pydata.org/generated/seaborn.violinplot.html
# inner{“box”, “quartile”, “point”, “stick”, None}, optional
ax = sns.violinplot(data=data, scale='area', inner='box')

x_tick_labels = ["Cat {}".format(i + 1) for i in range(num_category)]
ax.set_xticklabels(x_tick_labels)
# ax.set_yticklabels(y_tick_labels)
# plt.yticks(rotation=0)
# # ax.ticklabel_format(axis='both', style='sci')
# # ax.set_yscale("log")

ax.tick_params(length=0, top=False, bottom=False, left=False, right=False, 
    labelleft=True, labelbottom=True, labelsize=12)
ax.set_xlabel('ax_xlabel', fontsize=16, labelpad=10)
ax.set_ylabel('ax_ylabel', fontsize=16, labelpad=10)
ax.set_title('Violin plot', fontsize=16)
# plt.text(2, len(y_tick_labels) + 2, "Linear Heatmap", fontsize=16)

plt.savefig('../images/violin_plot_multiple.png', transparent=False, dpi=200, bbox_inches="tight")

plt.show()