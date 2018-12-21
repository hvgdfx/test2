#
# import tensorflow as tf
#
# path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
#
# text = open(path_to_file).read()
#
# print(type(text))
#
#
#coding:utf-8
from __future__ import print_function

from keras.layers import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
from keras.utils.vis_utils import plot_model
import numpy as np


def process_txt(open_path):
    with open(open_path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            line = line.strip().lower()
            # line = line.decode("ascii", "ignore")
            if 0 == len(line):
                continue
            lines.append(line)
    text = ' '.join(lines)
    return text

text = process_txt('hongloumeng.txt')

len(text)



chars = set([c for c in text])
chars_count = len(chars)
char2index = dict((c, i) for i, c in enumerate(chars))
index2char = dict((i, c) for i, c in enumerate(chars))


SEQLEN = 10
STEP = 1
input_chars = []
label_chars = []
for  i in range(0, len(text) - SEQLEN, STEP):
    input_chars.append(text[i:i+SEQLEN])
    label_chars.append(text[i+SEQLEN])


X = np.zeros((len(input_chars), SEQLEN, chars_count), dtype=np.bool)
Y = np.zeros((len(input_chars), chars_count), dtype=np.bool)
for i,input_char in enumerate(input_chars):
    for j,c in enumerate(input_char):
        X[i, j, char2index[c]] = 1
    Y[i, char2index[label_chars[i]]] = 1



HIDDEN_SIZE = 128
BATCH_SIZE = 128
NUM_ITERATIONS = 1000
NUM_EPOCHS_PER_ITERATION = 1
NUM_PREDS_PER_EPOCH = 100

model = Sequential()
model.add(SimpleRNN(HIDDEN_XSIZE, return_sequences=False,
                    input_shape=(SEQLEN, chars_count),unroll=True))
model.add(Dense(chars_count))
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")



for iteration in range(NUM_ITERATIONS):
    print('Iteration : %d'%iteration)
    model.fit(X, Y, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS_PER_ITERATION)
    # 训练1epoch,测试一次
    test_idx = np.random.randint(len(input_chars))
    test_chars = input_chars[test_idx]
    print('test seed is : %s'%test_chars)
    print(test_chars,end='')
    for i in range(NUM_PREDS_PER_EPOCH):
        # 测试序列向量化
        vec_test = np.zeros((1, SEQLEN, chars_count))
        for i, ch in enumerate(test_chars):
            vec_test[0, i, char2index[ch]] = 1
        pred = model.predict(vec_test, verbose=0)[0]
        pred_char = index2char[np.argmax(pred)]
        print(pred_char,end='')
        # 不断的加入新生成字符组成新的序列
        test_chars = test_chars[1:] + pred_char
    print('\n')



#
# classes = model.predict(X, batch_size=1)
# print('--------------------------')
# print(X.shape)
# print(classes.shape)
# print('--------------------------')
