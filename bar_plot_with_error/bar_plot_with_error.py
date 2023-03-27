import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import seaborn as sns
sns.set_theme(style="whitegrid")

# plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-deep')
# plt.style.use('fivethirtyeight')

def reverse(in_list):
    return list(reversed(in_list))

if __name__ == "__main__":

    data_num = 18
    data = [np.random.randint(low=1,high=10) for i in range(data_num)] 
    # data = np.reshape(data, (1, 8))
    x_tick_labels = ["x {}".format(i + 1) for i in range(data_num)]
    legend_labels = ["L {}".format(i + 1) for i in range(data_num)]

    # plt.figure(figsize=(16,4))
    fig, ax = plt.subplots(1, 1, figsize=(8, 3))#, sharex=True)
    # ax.bar(x_tick_labels, data)

    # color palatte: https://seaborn.pydata.org/tutorial/color_palettes.html
    sns.barplot(x=x_tick_labels, y=data, ax=ax)
    plt.errorbar(x_tick_labels, data, yerr=0.1*np.array(data), fmt=',', ecolor='black', capsize=2)

    label_font = 14
    tick_font = 12
    legend_font = 12

    # ax.legend(legend_labels, loc=(0.5, 1.2), fontsize=legend_font)

    # remove frame
    # for spine in ax.spines.values():
    #     spine.set_visible(False)

    # ax.get_xaxis().set_visible(False)

    ax.set_xticklabels(x_tick_labels, fontsize=tick_font)
    plt.xticks(rotation=50)

    ax.tick_params(length=5, top=False, bottom=False, left=False, right=False, 
        labelleft=True, labelbottom=True, labelsize=tick_font)

    ax.set_ylabel('ax_ylabel', fontsize=label_font)

    plt.rcParams.update({'figure.autolayout': True})

    plt.savefig('../images/bar_plot_with_error.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
