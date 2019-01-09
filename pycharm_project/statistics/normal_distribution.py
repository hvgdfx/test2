


import numpy as np
import matplotlib.pyplot as plt

sample_num = 100000
sample_dim = 10

alist = np.zeros(shape=[sample_num, sample_dim])

for i in range(sample_num):
    for j in range(sample_dim):
        x = np.random.randint(10)
        alist[i, j] = x

alist_ave = alist.sum(axis=1)
aset = set(alist_ave)

adict = {}

for i in alist_ave:
    if i not in adict:
        adict[i] = 1
    else:
        adict[i] += 1

print(adict)

plt.scatter(adict.keys(), adict.values())
plt.show()


