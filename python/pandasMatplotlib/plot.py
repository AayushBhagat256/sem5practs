import matplotlib.pyplot as plt
import numpy as np

x = np.array(["a","b","c","d"])
y = np.array([12,2,56,34])

plt.bar(x,y)
plt.show()

plt.pie(y,labels=x)
plt.show()

plt.hist(y)
plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)
plt.show()