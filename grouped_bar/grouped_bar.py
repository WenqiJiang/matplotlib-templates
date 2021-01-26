import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

x_labels = ['G1', 'G2', 'G3', 'G4', 'G5']
y_men_means = [20, 34, 30, 35, 27]
y_women_means = [25, 32, 34, 20, 25]

x = np.arange(len(x_labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1  = ax.bar(x - width/2, y_men_means, width)#, label='Men')
rects2 = ax.bar(x + width/2, y_women_means, width)#, label='Women')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend([rects1, rects2], ["Men", "Women"], loc="upper right", ncol=1, \
  facecolor='white', framealpha=1, frameon=False)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.rcParams.update({'figure.autolayout': True})

plt.savefig('../images/grouped_bar.png', transparent=False, dpi=200, bbox_inches="tight")
plt.show()
