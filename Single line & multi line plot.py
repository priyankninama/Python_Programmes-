#Single line
import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,4,9]


plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Line Graph')

plt.show()

#Double Line
import matplotlib.pyplot as plt1

x1 = [1,2,3]
y1 = [2,4,1]
plt1.plot(x1, y1, label = "line 1")

x2 = [1,2,3]
y2 = [4,1,3]
plt1.plot(x2, y2, label = "line 2")

plt1.xlabel('x - axis')
plt1.ylabel('y - axis')
plt1.title('Two lines graph!')
plt1.legend()

plt1.show()

#curve 
import matplotlib.pyplot as plt2
import numpy as np
  
x = np.arange(0, 2*(np.pi), 0.1)

y = np.sin(x)
  
plt2.plot(x, y)

plt2.show()

#scatter chart
import matplotlib.pyplot as plt3

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,5,7,6,8,9,11,12,12]

plt3.scatter(x, y, label= "stars", color= "blue", marker= "+", s=30)

plt3.xlabel('x - axis')
plt3.ylabel('y - axis')
plt3.title('My scatter plot!')
plt3.legend()

plt3.show()
