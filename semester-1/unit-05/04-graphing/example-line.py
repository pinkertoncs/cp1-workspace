import matplotlib.pyplot as plt

# create a subplot, (1 row , 1 col) aka. 1 plot
# this enables us to change ticks and labels
fig, ax = plt.subplots(1, 1)

# graph labels
labels = ['Chicken', 'Fish', 'Steak', 'Vegetarian']

# data
num_dishes = [34, 11, 47, 3]

# set the x  range/ tick to length of num_dishes
x = range(len(num_dishes))

# create the pie chart
ax.plot(x, num_dishes)

# set the ticks to number of dishes
ax.set_xticks(x)

# set the labels to the food item
ax.set_xticklabels(labels)

# show the graph
plt.show()