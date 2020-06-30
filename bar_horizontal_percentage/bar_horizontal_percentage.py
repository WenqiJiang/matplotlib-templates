import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import PercentFormatter


def reverse(in_list):
    return list(reversed(in_list))

if __name__ == "__main__":
    
    label = ["fp16", "fp32"]
    
    data_bar0_left = [16.29, 22.16]
    data_bar0_right = [11.23, 15.33]
    data_bar0_perc_left = [data_bar0_left[i] / (data_bar0_left[i] + data_bar0_right[i]) \
        for i in range(len(data_bar0_right))]
    data_bar0_perc_right = [data_bar0_right[i] / (data_bar0_left[i] + data_bar0_right[i]) \
        for i in range(len(data_bar0_right))]
        
    data_bar1_left = [22.16, 16.29]
    data_bar1_right = [13.23, 14.33]
    data_bar1_perc_left = [data_bar1_left[i] / (data_bar1_left[i] + data_bar1_right[i]) \
        for i in range(len(data_bar1_right))]
    data_bar1_perc_right = [data_bar1_right[i] / (data_bar1_left[i] + data_bar1_right[i]) \
        for i in range(len(data_bar1_right))]
    
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(8,2.5))

    color_bar_left = '#1F1F1F'
    color_bar_right = '#9F9F9F'
    label_font = 14
    legend_font = 14
    tick_font = 14
    text_font = 14

    bar_ax0_left = ax0.barh(reverse(label), reverse(data_bar0_perc_left), color=color_bar_left)
    bar_ax0_right = ax0.barh(reverse(label), reverse(data_bar0_perc_right), 
        left=reverse(data_bar0_perc_left), color=color_bar_right)#, hatch="+"*2)
    
    bar_ax1_left = ax1.barh(reverse(label), reverse(data_bar1_perc_left), color=color_bar_left)
    bar_ax1_right = ax1.barh(reverse(label), reverse(data_bar1_perc_right), 
        left=reverse(data_bar1_perc_left), color=color_bar_right)#, hatch="-"*2)

    ax0.legend([bar_ax0_left, bar_ax0_right] , ["Legend: bar_ax0_left", "Legend: bar_ax0_right"], 
        loc=(0.62, 1.1), fontsize=legend_font)

    for i, v in enumerate(reverse(data_bar0_left)):
        ax0.text(1.01, i - 0.1, "{:.2f} unit".format(v + data_bar0_right[i]), fontsize=text_font)

    for i, v in enumerate(reverse(data_bar1_left)):
        ax1.text(1.01, i - 0.1, "{:.2f} unit".format(v + data_bar1_right[i]), fontsize=text_font)

    # remove frame
    for spine in ax0.spines.values():
        spine.set_visible(False)

    ax0.get_xaxis().set_visible(False)
    ax0.set_yticks(label)
    ax0.tick_params(length=5, top=False, bottom=False, left=False, right=False, 
        labelleft=True, labelbottom=True, labelsize=tick_font)
    ax0.set_ylabel('ax0_ylabel', fontsize=label_font, labelpad=24, rotation=60)

    # remove frame
    for spine in ax1.spines.values():
        spine.set_visible(False)
    ax1.set_ylabel('ax1_ylabel', fontsize=label_font, labelpad=20, rotation=60)
    ax1.set_xlabel("ax1_xlabel", fontsize=label_font, labelpad=10)

    plt.rcParams.update({'figure.autolayout': True})
    ax1.tick_params(length=5, top=False, bottom=True, left=False, right=False, 
        labelleft=True, labelbottom=True, labelsize=tick_font)
    
    def percentage(x, pos):
        """The two args are the value and tick position"""
        return '{}%'.format(int(x * 100))

    formatter = FuncFormatter(percentage)
    ax0.xaxis.set_major_formatter(formatter)
    ax1.xaxis.set_major_formatter(formatter)

    plt.savefig('../images/bar_horizontal_percentage.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
