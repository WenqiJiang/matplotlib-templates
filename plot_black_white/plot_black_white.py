import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter

# plt.style.use('grayscale')

if __name__ == "__main__":

    """ TODO: adjust figure size when needed """
    fig, ax = plt.subplots(1, 1, figsize=(8, 3))

    """ TODO: edit the plot data, both x and y """
    data_y_plot0 = np.array([10, 20, 30, 40, 50])
    data_y_plot1 = np.array([10, 20, 30, 40, 50]) + 10
    data_y_plot2 = np.array([10, 20, 30, 40, 50]) + 20
    data_y_plot3 = np.array([10, 20, 30, 40, 50]) + 30
    data_y_plot4 = np.array([10, 20, 30, 40, 50]) + 40 
    data_y_plot5 = np.array([10, 20, 30, 40, 50]) + 50

    data_x = [1, 4, 5, 8, 9]

    """ TODO: adjust label font / tick font / marker size when needed """
    label_font = 18
    legend_font = 14
    tick_font = 14

    markersize = 8


    """ TODO: remove unnedded plot, and select marker style for it """
    plot0 = ax.plot(data_x, data_y_plot0, marker="D", fillstyle="full", markerfacecolor='black', markersize=markersize, color='black')
    plot1 = ax.plot(data_x, data_y_plot1, marker="D", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot2 = ax.plot(data_x, data_y_plot2, marker="x", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot3 = ax.plot(data_x, data_y_plot3, marker="o", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot4 = ax.plot(data_x, data_y_plot4, marker="^", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')
    plot5 = ax.plot(data_x, data_y_plot5, marker="s", fillstyle="full", markerfacecolor='white', markersize=markersize, color='black')

    """ Note: add dotted line in Y axis """
    """ TODO: choose line style: dotted / dashed """
    ax.grid(axis='y', color='#777777', linestyle=(0, (1, 7.5)), linewidth=1) # dotted line
    # ax.grid(axis='y', color='#aaaaaa', linestyle=(0, (5, 6)), linewidth=1) # dashed line

    """ Note: add legend here, remove the frame of the legend """
    """ TODO: adjust the position, place it in the plot / above the plot """
    ax.legend([plot0[0], plot1[0], plot2[0], plot3[0], plot4[0], plot5[0]], 
        ["plot0_legend", "plot1_legend", "plot2_legend", "plot3_legend", "plot4_legend", "plot5_legend"], loc=(0, 1.05), ncol=3, 
        fontsize=legend_font, facecolor='white', framealpha=1, frameon=False)

    """ Note: Set ticks, enable left and bottom ticks, set label to left """
    """ TODO: adjust the length of major / minor tick if needed """
    ax.minorticks_on()
    ax.tick_params(top=False, bottom=True, left=True, right=False, labelleft=True, which='major', labelsize=tick_font, direction='in', length=8, width=1)
    ax.tick_params(top=False, bottom=True, left=True, right=False, which='minor', labelsize=tick_font, direction='in', length=5, width=1)

    """ TODO: adjust the range of the ticks, set 3 ticks in y axis, both the major and minor ticks"""
    ax.yaxis.set_ticks([20, 60, 100])  
    ax.yaxis.set_ticks([40, 80, 120], minor=True) 
    ax.set_ylim([0, 110])

    """ TODO: remove x axis minor tick if needed """
    ax.xaxis.set_ticks(np.arange(1.5, 9, 1), minor=True) # 1/2 of the major
    # ax.xaxis.set_ticks(np.arange(1, 9, 1), minor=True) # remove (overlap with major)

    """ Note: Set labels """
    """ TODO: edit label text """
    ax.get_xaxis().set_visible(True)
    ax.set_xlabel('xlabel', fontsize=label_font)
    ax.set_ylabel('ylabel\n(unit)', fontsize=label_font)


    plt.rcParams.update({'figure.autolayout': True})

    """ TODO: adjust the output directory """
    plt.savefig('../images/plot_black_white.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()
