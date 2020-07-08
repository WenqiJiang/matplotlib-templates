import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter

if __name__ == "__main__":

    data_y_plot0 = [100, 80, 70, 50, 30]
    data_y_plot1 = [80, 60, 40, 30, 20]
    data_x = ["4", "8", "16", "32", "64"]

    fig, ax = plt.subplots(1, 1, figsize=(8, 4))

    label_font = 16
    markersize = 8
    tick_font = 14
    text_font = 16

    dark_grey = "#2F2F2F"
    color_plot0 = dark_grey
    color_plot1 = dark_grey

    plot0 = ax.plot(data_x, data_y_plot0, color=color_plot0, marker='o', markersize=markersize)
    plot1 = ax.plot(data_x, data_y_plot1, color=color_plot1, marker='^', markersize=markersize)

    ax.fill_between(data_x, data_y_plot0, data_y_plot1, hatch='/' * 2, edgecolor='black', linestyle='-', linewidth=2, color='#CFCFCF')
    
    ax.hlines(data_y_plot1[-1], "4", "64", color='#3F3F3F', linestyles='dashed')
    ax.text(0.3, data_y_plot1[-1] + 5, "{:.2f} x".format(data_y_plot1[-1]), fontsize=text_font)

    ax.hlines(data_y_plot0[0], "4", "64", color='#3F3F3F', linestyles='dashed')
    ax.text(1.3, data_y_plot0[0] + 5, "{:.2f} x".format(data_y_plot0[0]), fontsize=text_font)

    ax.annotate("annotation label", xy=(2, 55), xytext=(2.5, 80), arrowprops={"arrowstyle": '-|>', 'color': "#2f2f2f", 'linewidth': 2}, fontsize=text_font)

    ax.legend([plot0[0], plot1[0]], ["plot0_legend", "plot1_legend"], loc=(0.6, 0.95), fontsize=label_font, frameon=False)

    ax.tick_params(length=5, top=False, bottom=False, left=True, right=False, labelleft=True, labelsize=tick_font)
    ax.get_xaxis().set_visible(True)
    ax.set_xlabel('xlabel', fontsize=label_font, labelpad=5)
    ax.set_ylabel('ylabel', fontsize=label_font, labelpad=10)
    # ax.set(ylim=[0, 120])
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.rcParams.update({'figure.autolayout': True})

    plt.savefig('../images/plot_fill.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
