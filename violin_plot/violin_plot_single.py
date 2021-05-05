import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import seaborn as sns 

# Seaborn version >= 0.11.0

sns.set_theme(style="whitegrid")


# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

# print(data.shape)
# ax = sns.violinplot(x=["x axis"], y=["y axis"], data=data) # x, y only used in dataframe
ax = sns.violinplot(data=data)


# ax.set_xticklabels(x_tick_labels)
# ax.set_yticklabels(y_tick_labels)
# plt.yticks(rotation=0)
# # ax.ticklabel_format(axis='both', style='sci')
# # ax.set_yscale("log")

# ax.tick_params(length=0, top=False, bottom=False, left=False, right=False, 
#     labelleft=True, labelbottom=True, labelsize=12)
# ax.set_xlabel('ax_xlabel', fontsize=16, labelpad=10)
# ax.set_ylabel('ax_ylabel', fontsize=16, labelpad=10)
# # ax.set_title('Linear Heatmap', fontsize=16, y=5)
# plt.text(2, len(y_tick_labels) + 2, "Linear Heatmap", fontsize=16)

plt.savefig('../images/violin_plot_single.png', transparent=False, dpi=200, bbox_inches="tight")

plt.show()