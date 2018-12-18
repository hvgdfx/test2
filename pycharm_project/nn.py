

import tensorflow as tf
import numpy as np


# set config

train_x1_num = 10
train_x0_num = 10
train_dim = 5
train_num = train_x1_num + train_x0_num

weight1_dim = 3
weight2_dim = 2

# generate data

train_x1 = np.random.rand(train_x1_num, train_dim)
train_x0 = np.random.rand(train_x0_num, train_dim)*10
train_x = np.vstack((train_x1, train_x0))

train_y1 = np.ones([train_x1_num, 1])
train_y0 = np.zeros([train_x0_num, 1])
train_y = np.vstack((train_y1, train_y0))

# generate weight

weight1 = np.random.rand(train_dim, weight1_dim)
weight2 = np.random.rand(weight1_dim, weight2_dim)

b1 = np.random.rand(train_dim, 1)
b2 = np.random.rand(weight1_dim, 1)

# define function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    return 0

# forward-prop

a1 = np.dot(train_x, weight1)
h1 = sigmoid(a1)

a2 = np.dot(h1, weight2)
h2 = softmax(a2)

# define loss





if __name__ == '__main__':
    print(train_x)









