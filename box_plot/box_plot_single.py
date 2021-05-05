import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-deep')
# plt.style.use('fivethirtyeight')

# Fixing random state for reproducibility
np.random.seed(19680801)

# fake up some data
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot(data)

plt.show()

plt.rcParams.update({'figure.autolayout': True})
plt.savefig('../images/box_plot_single.png', transparent=False, dpi=200, bbox_inches="tight")