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


# Wenqi: flatten the table to a table. It's a dictionary with the key as schema.
#   The value of each key is an array.
# label category data
# xxx   xxx      xxx
# yyy   yyy      yyy

num_x_labels = 10
n_category = 3

d = {}
d['label'] = []
d['data'] = []
d['category'] = []

for j in range(n_category):
    data = []
    for i in range(num_x_labels):
        spread = np.random.rand(50) * 100
        center = np.ones(25) * 50 + 10 * j
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100
        partial_data = np.concatenate((spread, center, flier_high, flier_low))
        data.append(partial_data)

    for i in range(num_x_labels):
        # d['label'].append(i)
        for ele in data[i]:
            d['label'].append('label {}'.format(i))
            d['data'].append(ele)
            d['category'].append('category {}'.format(j))

df = pd.DataFrame(data=d)
print(df.index)
print(df.columns)

plt.figure(figsize=(12, 3))
# API: https://seaborn.pydata.org/generated/seaborn.violinplot.html
# inner{“box”, “quartile”, “point”, “stick”, None}, optional
ax = sns.violinplot(data=df, scale='area', inner='box', x="label", y="data", hue="category")

x_tick_labels = ["label {}".format(i + 1) for i in range(num_x_labels)]
ax.set_xticklabels(x_tick_labels)
# ax.set_yticklabels(y_tick_labels)
# plt.yticks(rotation=0)
# # ax.ticklabel_format(axis='both', style='sci')
# # ax.set_yscale("log")
ax.legend(loc='upper right')

ax.tick_params(length=0, top=False, bottom=False, left=False, right=False, 
    labelleft=True, labelbottom=True, labelsize=12)
ax.set_xlabel('ax_xlabel', fontsize=16, labelpad=10)
ax.set_ylabel('ax_ylabel', fontsize=16, labelpad=10)
ax.set_title('Violin plot', fontsize=16)
# plt.text(2, len(y_tick_labels) + 2, "Linear Heatmap", fontsize=16)

plt.savefig('../images/violin_plot_multi_class.png', transparent=False, dpi=200, bbox_inches="tight")

plt.show()