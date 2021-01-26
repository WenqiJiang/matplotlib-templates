import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter

plt.style.use('ggplot')

if __name__ == "__main__":

    data_y_plot0 = [100, 20, 80, 50, 70]
    data_y_plot1 = [80, 90, 45, 23, 100]
    data_x = [1, 4, 5, 8, 9]

    fig, ax = plt.subplots(1, 1, figsize=(8, 3))

    label_font = 16
    markersize = 8
    tick_font = 14
    color_plot0 = "#008A00"
    color_plot1 = "#1BA1E2"

    plot0 = ax.plot(data_x, data_y_plot0)#, color=color_plot0, marker='o', markersize=markersize)
    plot1 = ax.plot(data_x, data_y_plot1)#, color=color_plot1, marker='^', markersize=markersize)
    ax.legend([plot0[0], plot1[0]], ["plot0_legend", "plot1_legend"], loc='upper right', fontsize=label_font)
    ax.tick_params(top=False, bottom=True, left=True, right=False, labelleft=True, labelsize=tick_font)
    ax.get_xaxis().set_visible(True)
    ax.set_xlabel('xlabel', fontsize=label_font)
    ax.set_ylabel('ylabel', fontsize=label_font)

    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)

    plt.rcParams.update({'figure.autolayout': True})

    plt.savefig('../images/plot_with_style.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
