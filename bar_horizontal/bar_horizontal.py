import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def reverse(in_list):
    return list(reversed(in_list))

if __name__ == "__main__":

    label = ["1", "8", "32", "64", "128", "256"]

    data_bar0_left = [9.925, 11.192, 10.467, 11.057, 13.014, 18.256]
    data_bar0_right = [8.699, 9.368, 8.542, 9.019, 10.004, 13.305]

    data_bar1_left = [20.488,  23.375, 20.799, 21.854, 23.816, 31.988]
    data_bar1_right = [18.164, 20.849, 18.374, 19.404, 20.430, 26.555]

    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8, 4))

    color_bar_left = '#B85450'
    color_bar_right = '#F8CECC'

    bar_ax0_left = ax0.barh(reverse(label), reverse(data_bar0_left), color=color_bar_left)
    bar_ax0_right = ax0.barh(reverse(label), reverse(data_bar0_right), 
        left=reverse(data_bar0_left), color=color_bar_right)

    bar_ax1_left = ax1.barh(reverse(label), reverse(data_bar1_left), color=color_bar_left)
    bar_ax1_right = ax1.barh(reverse(label), reverse(data_bar1_right), 
        left=reverse(data_bar1_left), color=color_bar_right)

    label_font = 15
    tick_font = 13
    legend_font = 14

    ax0.legend([bar_ax0_left, bar_ax0_right] , ["Legend: bar_ax0_left", "Legend: bar_ax0_right"], 
        loc=(0.5, 1.2), fontsize=legend_font)

    # remove frame
    for spine in ax0.spines.values():
        spine.set_visible(False)

    ax0.get_xaxis().set_visible(False)
    ax0.set_yticks(label)
    ax0.tick_params(length=5, top=False, bottom=True, left=False, right=False, 
        labelleft=True, labelbottom=False, labelsize=tick_font)
    ax0.set_ylabel('ax0_ylabel', fontsize=label_font)

    # remove frame
    for spine in ax1.spines.values():
        spine.set_visible(False)
    ax1.set_ylabel('ax1_ylabel', fontsize=label_font)
    ax1.set_xlabel('ax1_xlabel', fontsize=label_font)
    ax1.tick_params(length=5, top=False, bottom=True, left=False, right=False, 
        labelleft=True, labelbottom=True, labelsize=tick_font)

    plt.rcParams.update({'figure.autolayout': True})

    plt.savefig('../images/bar_horizontal.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
