

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


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
    a, b = x.shape
    return np.exp(x)/np.exp(x).sum(axis=1).reshape(a, 1)

# forward-propagete

a1 = np.dot(train_x, weight1)
h1 = sigmoid(a1)

a2 = np.dot(h1, weight2)
h2 = softmax(a2)

# define loss


def log_loss(y_true, y_pred):
    from sklearn.metrics import log_loss
    return log_loss(y_true, y_pred)


# back-progagete



# plot loss


def plot_loss(x):
    pass


from sklearn.metrics import log_loss

# run server

if __name__ == '__main__':
    a = np.random.rand(3, 2)
    b = np.exp(a)
    print(a)
    print(b)
    c = np.exp(a).sum(axis=1).reshape(3, 1)
    print(c)
    print(h2)









