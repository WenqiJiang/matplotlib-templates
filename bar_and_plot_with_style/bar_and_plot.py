import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')
plt.style.use('seaborn-deep')
# plt.style.use('fivethirtyeight')


if __name__ == "__main__":

    data_bar_lower0 = [1,2,3]
    data_bar_upper0 = [2,1,3]
    data_plot0 = [100, 20, 70]
    label0 = ["1", "8", "32"]

    data_bar_lower1 = [4,5,6]
    data_bar_upper1 = [4,1,3]
    data_plot1 = [80, 90, 100]
    label1 = ["4", "16", "64"]

    label_font = 15
    tick_font = 13
    legend_font = 14

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(8, 3), sharex=True)

##############################     bar      ##############################

    color_bar_lower = '#2BC0FF'
    color_bar_lower_edge = "#0F97FF"
    color_bar_upper = '#DAE8FC'
    color_bar_upper_edge = "#CADAFC"

    ax0_bar_lower = ax0.bar(label0, data_bar_lower0)
        # , color=color_bar_lower, 
        # edgecolor=color_bar_lower_edge, hatch='+'*2)
    ax0_bar_upper = ax0.bar(label0, data_bar_upper0, bottom=data_bar_lower0)#, 
        # color=color_bar_upper, edgecolor=color_bar_upper_edge)

    ax1_bar_lower = ax1.bar(label1, data_bar_lower1)#, 
        # color=color_bar_lower, edgecolor=color_bar_lower_edge, hatch='+'*2)
    ax1_bar_upper = ax1.bar(label1, data_bar_upper1)#, 
        # bottom=data_bar_lower1, color=color_bar_upper, edgecolor=color_bar_upper_edge)

##############################     plot      ##############################

    # twinx: Create a twin Axes sharing the xaxis
    ax0_twinx = ax0.twinx() 
    ax1_twinx = ax1.twinx() 

    legend_marker = '^'
    legend_color = "#4D9900"
    markersize = 8

    ax0_plot = ax0_twinx.plot(label0, data_plot0)#, color=legend_color, 
        # marker=legend_marker, markersize=markersize)
    ax1_plot = ax1_twinx.plot(label1, data_plot1)#, color=legend_color, 
        # marker=legend_marker, markersize=markersize)

##############################     bar setting      ##############################
    # remove frame
    for spine in ax0.spines.values():
        spine.set_visible(False)

    ax0.get_yaxis().set_visible(False)
    ax0.set_xticks(label0)
    ax0.tick_params(length=5, top=False, bottom=False, left=False, right=False, 
        labelleft=False, labelbottom=True, labelsize=tick_font)
    ax0.set_xlabel('ax0_xlabel', fontsize=label_font, labelpad=10)

    # remove frame
    for spine in ax1.spines.values():
        spine.set_visible(False)
    ax1.set_xlabel('ax1_xlabel', fontsize=label_font, labelpad=10)
    ax1.set_ylabel('ax1_ylabel', fontsize=label_font, labelpad=10)
    ax1.tick_params(length=5, top=False, bottom=False, left=False, right=False, 
        labelleft=False, labelright=True, labelbottom=True, labelsize=tick_font)
    ax1.yaxis.set_label_position("right")
    ax1.yaxis.tick_right()

##############################     plot setting     ##############################
    
    for spine in ax0_twinx.spines.values():
        spine.set_visible(False)
    ax0_twinx.set_ylabel('ax0_twinx_ylable', fontsize=label_font, labelpad=10)
    ax0_twinx.yaxis.set_label_position("left")
    ax0_twinx.tick_params(length=5, top=False, bottom=False, left=True, 
        right=False, labelleft=True, labelright=False, labelbottom=False, labelsize=tick_font)

    for spine in ax1_twinx.spines.values():
        spine.set_visible(False)
    ax1_twinx.tick_params(length=5, top=False, bottom=False, left=False, 
        right=False, labelleft=False, labelright=False, labelbottom=False, labelsize=tick_font)

##############################     finish up      ##############################

    ax1.legend([ax0_bar_lower, ax0_bar_upper, ax0_plot[0]], 
        ["legend: ax0_bar_lower", "legend: ax0_bar_upper", "legend: ax0_plot"], 
        loc=(0, 1.1), fontsize=legend_font)

    plt.rcParams.update({'figure.autolayout': True})
    plt.savefig('../images/bar_and_plot_with_style.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
