

import matplotlib.pyplot as plt
import numpy as np

# 3 steps

x1 = range(1, 10)
y1 = range(1, 10)

x2 = range(10, 20)
y2 = range(10, 20)


fig = plt.figure()


#
# plt.plot(x1, y1)
# plt.plot(x2, y2)

ax1 = fig.add_subplot(2, 3, 1)
plt.scatter(x1, y1)

# ax2 = fig.add_subplot(235)
plt.bar(x1, y1)

# ax3 = fig.add_subplot(233)
plt.hist(x1, y1)

#
# plt.plot()
# plt.show()


img = plt.imread('D:/zgx/zgx/pycharm_project/timg.jpg')

img.setflags(write=True)

ax2 = fig.add_subplot(2, 3, 3)

plt.imshow(img)

plt.show()
