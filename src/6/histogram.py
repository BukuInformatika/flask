import matplotlib.pyplot as plt
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,.....309]
num_bins =6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'green')
plt.show()