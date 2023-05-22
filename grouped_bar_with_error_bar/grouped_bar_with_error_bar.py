import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('ggplot')
plt.style.use('seaborn-colorblind') 

x_labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# 3 runs each
y_men = {'G1': [3,4,5], 'G2': [5,6,7], 'G3':[4,5,5], 'G4': [8,5,3], 'G5': [5,6,1]}
y_women = {'G1': [3,4,8], 'G2': [5,6,6], 'G3':[6,5,5], 'G4': [8,5,6], 'G5': [5,6,3]}

def get_error_bar(d):
    """
    Given the key, return a dictionary of std deviation
    """
    dict_error_bar = dict()
    for key in d:
        array = d[key]
        dict_error_bar[key] = np.std(array)
    return dict_error_bar

def get_mean(d):
    """
    Given the key, return a dictionary of mean
    """
    dict_mean = dict()
    for key in d:
        array = d[key]
        dict_mean[key] = np.average(array)
    return dict_mean

def get_y_array(d, keys):
    """
    Given a dictionary, and a selection of keys, return an array of y value
    """
    y = []
    for key in keys:
        y.append(d[key])
    return y


y_men_means = get_y_array(get_mean(y_men), x_labels)
y_women_means = get_y_array(get_mean(y_women), x_labels)

y_men_error_bar = get_y_array(get_error_bar(y_men), x_labels)
y_women_error_bar = get_y_array(get_error_bar(y_women), x_labels)

x = np.arange(len(x_labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1  = ax.bar(x - width/2, y_men_means, width)#, label='Men')
rects2 = ax.bar(x + width/2, y_women_means, width)#, label='Women')
ax.errorbar(x - width / 2, y_men_means, yerr=y_men_error_bar, fmt=',', ecolor='black', capsize=1.5)
ax.errorbar(x + width / 2, y_women_means, yerr=y_women_error_bar, fmt=',', ecolor='black', capsize=1.5)


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
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.rcParams.update({'figure.autolayout': True})

plt.savefig('../images/grouped_bar_with_error_bar.png', transparent=False, dpi=200, bbox_inches="tight")
plt.show()
