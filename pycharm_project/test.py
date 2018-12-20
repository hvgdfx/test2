from __future__ import print_function

import tensorflow as tf
from tensorflow import keras
#
fashion_mnist = keras.datasets.fashion_mnist
# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
# class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
#                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
#
# train_images = train_images / 255.0
# test_images = test_images / 255.0

#
#
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28, 28)),
#     keras.layers.Dense(128, activation=tf.nn.relu),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
#
# model.compile(optimizer=tf.train.AdamOptimizer(),
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# model.fit(train_images, train_labels, epochs=5, batch_size=100)
#
#
# test_loss, test_acc = model.evaluate(test_images, test_labels)
#
# print(test_loss, test_acc)
# print(type(train_images))
# print('finish')


# rnn
#
# modelRnn = keras.Sequential([
#     # keras.layers.Flatten(input_shape=[28, 28]),
#     keras.layers.SimpleRNN(10, input_shape=(1, 1, 2)),
#     keras.layers.Dense(10, activation=tf.nn.softmax)
# ])
#
#
# modelRnn.compile(
#     optimizer=tf.train.AdamOptimizer(),
#     loss = 'sparse_categorical_crossentropy',
#     metrics = ['accuracy']
# )
#
#
# modelRnn.fit(train_images, train_labels, epochs=5)


import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import SimpleRNN
from keras import initializers
from keras.optimizers import RMSprop

batch_size = 50
num_classes = 10
epochs = 5
hidden_units = 50

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train.reshape(-1, 28, 28)
x_test = x_test.reshape(-1, 28, 28)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print('Evaluate RNN...')
model = Sequential()
model.add(SimpleRNN(hidden_units,
                    kernel_initializer=initializers.RandomNormal(stddev=0.001),
                    recurrent_initializer=initializers.Identity(gain=1.0),
                    activation='relu',
                    input_shape=x_train.shape[1:]))
model.add(Dense(num_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop()
model.compile(loss='categorical_crossentropy',
              optimizer=rmsprop,
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

scores = model.evaluate(x_test, y_test, verbose=0)

print('RNN test score:', scores[0])
print('RNN test accuracy:', scores[1])






