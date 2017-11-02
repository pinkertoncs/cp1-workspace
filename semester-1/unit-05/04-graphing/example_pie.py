import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# graph labels
labels = ['Chicken', 'Fish', 'Steak', 'Vegetarian']

# data
num_dishes = [34, 11, 47, 3]

# colors for slices
colors = ['yellow', 'blue', 'red', 'green']

# create the pie chart
plt.pie(num_dishes, labels=labels, colors=colors)

# equal x and y increments
plt.axis('equal')

# save the graph
plt.savefig('piechart')
