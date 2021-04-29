#Bar chart
import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 24, 36, 40, 5]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'blue'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Bar chart!')

plt.show()

# Pie Chart
import matplotlib.pyplot as plt1

activities = ['Computer', 'IT', 'Civil', 'Auto']

slices = [8, 6, 5, 4]

colors = ['r', 'y', 'g', 'b']

plt1.pie(slices, labels = activities, colors=colors, startangle=90, shadow = True, explode = (0, 0, 0.1, 0), radius = 0.6, autopct = '%1.1f%%')
plt1.legend()
plt1.show()

