import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# graph labels
labels = ['Chicken', 'Fish', 'Steak', 'Vegetarian']

# data
num_dishes = [34, 11, 47, 3]

# get range of elements to plot
x = range(len(num_dishes))

# plot the data
plt.bar(x, num_dishes, align='center')

# label the xticks with the dish name
plt.xticks(x, labels)

# describe the y axis
plt.ylabel('Number of Dishes')

# save the graph
plt.savefig('barchart')
