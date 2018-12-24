

from keras.datasets import mnist, fashion_mnist, cifar, cifar10, cifar100
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation

print(type(mnist))

# (x_train, y_train), (x_test, y_test) = cifar.load_data()
#
#
# x_train = x_train/255.0
# y_train = y_train/255.0
#
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)
#
#
# model = Sequential()
# model.add(LSTM(
#     128,
#     input_shape = (28, 28)
# ))
#
# model.add(
#     Dense(10, activation='relu')
# )
#
#
# model.compile(
#     optimizer='adam',
#     loss='categorical_crossentropy',
#     metrics= ['accuracy']
# )
#
# model.fit(x_test, y_test, epochs=3,
#           # steps_per_epoch=60
#           batch_size=128
#           )
#



