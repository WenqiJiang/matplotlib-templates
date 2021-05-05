import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter
import matplotlib.font_manager

hfont = {'fontname':'Helvetica'}

""" Note: set font style """
# print(plt.rcParams.keys())
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica']

if __name__ == "__main__":

    """ TODO: adjust figure size when needed """
    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(8, 10))

    """ TODO: edit the plot data, both x and y """
    data_y_plot0_0 = np.array([10, 20, 30, 40, 50])
    data_y_plot0_1 = np.array([10, 20, 30, 40, 50]) + 10
    data_y_plot0_2 = np.array([10, 20, 30, 40, 50]) + 20

    data_y_plot1_0 = np.array([10, 20, 30, 40, 50]) + 30
    data_y_plot1_1 = np.array([10, 20, 30, 40, 50]) + 40 
    data_y_plot1_2 = np.array([10, 20, 30, 40, 50]) + 50

    data_y_plot2_0 = np.array([10, 20, 30, 40, 50]) + 60
    data_y_plot2_1 = np.array([10, 20, 30, 40, 50]) + 70 
    data_y_plot2_2 = np.array([10, 20, 30, 40, 50]) + 80

    data_x = [1, 4, 5, 8, 9]

    """ TODO: adjust label font / tick font / marker size when needed """
    # font_size = 15
    label_font = 18
    legend_font = 16
    tick_font = 14
    subplot_title_font = 16

    markersize = 8

    """ TODO: remove unnedded plot, and select marker style for it """
    plot0_0 = ax0.plot(data_x, data_y_plot0_0, marker="D", fillstyle="full", markerfacecolor='black', markersize=markersize, color='black')
    plot0_1 = ax0.plot(data_x, data_y_plot0_1, marker="D", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot0_2 = ax0.plot(data_x, data_y_plot0_2, marker="x", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')

    plot1_0 = ax1.plot(data_x, data_y_plot1_0, marker="D", fillstyle="full", markerfacecolor='black', markersize=markersize, color='black')
    plot1_1 = ax1.plot(data_x, data_y_plot1_1, marker="D", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot1_2 = ax1.plot(data_x, data_y_plot1_2, marker="x", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')

    plot2_0 = ax2.plot(data_x, data_y_plot2_0, marker="D", fillstyle="full", markerfacecolor='black', markersize=markersize, color='black')
    plot2_1 = ax2.plot(data_x, data_y_plot2_1, marker="D", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot2_2 = ax2.plot(data_x, data_y_plot2_2, marker="x", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')


    """ Note: add dotted line in Y axis """
    """ TODO: choose line style: dotted / dashed """
    ax0.grid(axis='both', color='#777777', linestyle=(0, (1, 7.5)), linewidth=1) # dotted line
    ax1.grid(axis='both', color='#777777', linestyle=(0, (1, 7.5)), linewidth=1) # dotted line
    ax2.grid(axis='both', color='#777777', linestyle=(0, (1, 7.5)), linewidth=1) # dotted line
    # ax0.grid(axis='y', color='#aaaaaa', linestyle=(0, (5, 6)), linewidth=1) # dashed line
    # ax1.grid(axis='y', color='#aaaaaa', linestyle=(0, (5, 6)), linewidth=1) # dashed line
    # ax2.grid(axis='y', color='#aaaaaa', linestyle=(0, (5, 6)), linewidth=1) # dashed line

    """ Note: add legend here, remove the frame of the legend """
    """ TODO: adjust the position, place it in the plot / above the plot / other axes """
    legend_font_style = matplotlib.font_manager.FontProperties(family='sans-serif', style='normal', size=legend_font)
    ax0.legend([plot0_0[0], plot0_1[0], plot0_2[0]], 
        ["plot0_legend", "plot1_legend", "plot2_legend"], loc=(-0.05, 1.05), ncol=3, 
        fontsize=legend_font, facecolor='white', framealpha=1, frameon=False, prop=legend_font_style)

    """ Note: Set ticks, enable left and bottom ticks, set label to left, only the bottom plot has bottom tick """
    """ TODO: adjust the length of major / minor tick if needed """
    ax0.minorticks_on()
    ax1.minorticks_on()
    ax2.minorticks_on()

    ax0.tick_params(top=False, bottom=False, left=True, right=False, labelbottom=False, labelleft=True, which='major', labelsize=tick_font, direction='in', length=8, width=1)
    ax1.tick_params(top=False, bottom=False, left=True, right=False, labelbottom=False, labelleft=True, which='major', labelsize=tick_font, direction='in', length=8, width=1)
    ax2.tick_params(top=False, bottom=True, left=True, right=False, labelbottom=True, labelleft=True, which='major', labelsize=tick_font, direction='in', length=8, width=1)

    ax0.tick_params(top=False, bottom=False, left=True, right=False, which='minor', labelsize=tick_font, direction='in', length=5, width=1)
    ax1.tick_params(top=False, bottom=False, left=True, right=False, which='minor', labelsize=tick_font, direction='in', length=5, width=1)
    ax2.tick_params(top=False, bottom=True, left=True, right=False, which='minor', labelsize=tick_font, direction='in', length=5, width=1)

    """ TODO: adjust the range of the ticks, set 3 ticks in y axis, both the major and minor ticks"""
    ax0.yaxis.set_ticks([10, 40, 70])  
    ax0.yaxis.set_ticks([25, 55], minor=True) 
    ax0.set_ylim([0, 80])

    ax1.yaxis.set_ticks([40, 70, 100])  
    ax1.yaxis.set_ticks([55, 85], minor=True) 
    ax1.set_ylim([30, 110])

    ax2.yaxis.set_ticks([70, 100, 130])  
    ax2.yaxis.set_ticks([85, 115], minor=True) 
    ax2.set_ylim([60, 140])

    """ Note: only the bottom plot show x ticks """
    """ TODO: remove x axis minor tick if needed """
    ax2.xaxis.set_ticks(np.arange(1, 10, 1)) # 1/2 of the major
    ax2.xaxis.set_ticks(np.arange(1.5, 9, 1), minor=True) # 1/2 of the major
    # ax2.xaxis.set_ticks(np.arange(1, 9, 1), minor=True) # remove (overlap with major)

    """ TODO: edit plot name and position, note the position is absolute value """
    ax0.text(2, 60, '(a) Plot A', fontsize=subplot_title_font, horizontalalignment='center')
    ax1.text(2, 90, '(b) Plot B', fontsize=subplot_title_font, horizontalalignment='center')
    ax2.text(2, 120, '(c) Plot C', fontsize=subplot_title_font, horizontalalignment='center')

    """ Note: Set labels """
    """ TODO: edit label text """
    ax0.get_xaxis().set_visible(True)
    ax0.set_ylabel('ylabel\n(unit)', fontsize=label_font)
    ax1.set_ylabel('ylabel\n(unit)', fontsize=label_font)
    ax2.set_ylabel('ylabel\n(unit)', fontsize=label_font)
    ax2.set_xlabel('xlabel', fontsize=label_font)

    plt.rcParams.update({'figure.autolayout': True})



    # matplotlib.rcParams['font.family'] = 'serif'
    # matplotlib.rcParams['font.sans-serif'] = ['Times New Roman']

    """ TODO: adjust the output directory """
    plt.savefig('../images/subplots_black_white.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
