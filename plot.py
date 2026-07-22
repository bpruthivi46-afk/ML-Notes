import matplotlib.pyplot as plt


ages = [25, 30, 35, 40, 45, 50, 55, 60]
bins = [20, 30, 40, 50, 60]
plt.hist(ages, bins=bins, edgecolor='black', linewidth=1.5, color = '#f7e9d3')
plt.xlabel('Age')
plt.ylabel('frequency')
plt.title('Age Distribution')
plt.show()