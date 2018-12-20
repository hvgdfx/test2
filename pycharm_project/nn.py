

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

#train_y1 = np.ones([train_x1_num, 1])
train_y1 = [1] * train_x1_num
#train_y0 = np.zeros([train_x0_num, 1])
train_y0 = [0] * train_x0_num
#train_y = np.vstack((train_y1, train_y0))
train_y = train_y1 + train_y0

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

def binaray(x):
    char_2_in = dict((c, i) for i, c in enumerate(set(x)))
    in_2_char = dict((i, c) for i, c in enumerate(set(x)))
    # output = np.zeros([train_num, len(set(x))])
    output = np.array([[1e-15] * len(set(x))] * train_num)
    for i in range(train_num):
        output[i, char_2_in[x[i]]] = 1
    return output


for i in range(2):
    print('--------------{0}--------------'.format(i))


# caculate loss



# back-progagete


#dJdA2 = np.multiply(-1*h2[:, 1], h2*(1-h2))

from sklearn.metrics import log_loss



# tf

def tf_implement():
    import tensorflow as tf
    from tensorflow import keras

    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5, batch_size=100)

    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print(test_loss, test_acc)

# run server

if __name__ == '__main__':
    # print(np.multiply((binaray(train_y)-h2),binaray(train_y)))
    # print(binaray(train_y))
    # print(train_y)
    # print(h2)
    # print()
    # print(h2[:, 1] - train_y)








