from __future__ import print_function

import tensorflow as tf
from tensorflow import keras
#
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

modelRnn = keras.Sequential([
    # keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.SimpleRNN(128, input_shape=(28, 28)),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])


modelRnn.compile(
    optimizer=tf.train.AdamOptimizer(),
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)


modelRnn.fit(train_images, train_labels, epochs=30, batch_size=128)


test_loss, test_acc = modelRnn.evaluate(test_images, test_labels)

print(test_loss, test_acc)
print(type(train_images))
print('finish')





