import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x_labels = ['G1', 'G2', 'G3', 'G4', 'G5']

bar1_lower_height = [20, 34, 30, 35, 27]
bar1_upper_height = [10, 17, 15, 15, 17]

bar2_lower_height = [25, 32, 34, 20, 25]
bar2_upper_height = [15, 12, 14, 10, 15]

x = np.arange(len(x_labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1_lower  = ax.bar(x - width/2, bar1_lower_height, width)#, label='bar 1 lower')
rects1_upper  = ax.bar(x - width/2, bar1_upper_height, width, bottom=bar1_lower_height)#, label='bar 1 higher')
rects2_lower = ax.bar(x + width/2, bar2_lower_height, width)#, label='bar 2 lower')
rects2_upper = ax.bar(x + width/2, bar2_upper_height, width, bottom=bar2_lower_height)#, label='bar 2 higher')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

ax.legend([rects1_lower, rects1_upper, rects2_lower, rects2_upper], ["A", "B", "C", "D"], loc=(0.2, 1.05), ncol=4, \
  facecolor='white', framealpha=1, frameon=False)



def number_single_bar(rects, bottom):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height + bottom[i]),
                    xytext=(0, -20),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def number_stacked_bar(rects, bottom):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for i, rect in enumerate(rects):
        height = rect.get_height()
        ax.annotate('{}'.format(height + bottom[i]),
                    xy=(rect.get_x() + rect.get_width() / 2, height + bottom[i]),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

zero_bottom = np.zeros(5)

number_single_bar(rects1_lower, zero_bottom)
number_single_bar(rects1_upper, bar1_lower_height)
number_single_bar(rects2_lower, zero_bottom)
number_single_bar(rects2_upper, bar2_lower_height)

number_stacked_bar(rects1_upper, bar1_lower_height)
number_stacked_bar(rects2_upper, bar2_lower_height)

plt.rcParams.update({'figure.autolayout': True})

plt.savefig('../images/stacked_grouped_bar.png', transparent=False, dpi=200, bbox_inches="tight")
plt.show()
