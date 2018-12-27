from pandas import DataFrame
from keras import Sequential
from keras.layers import LSTM, Dense

# convert sequence to x/y pairs ready for use with an LSTM
def to_lstm_dataset(sequence, n_unique):
    encoded = encode(sequence, n_unique)
    X, y = to_xy_pairs(encoded)
    dfX, dfy = DataFrame(X), DataFrame(y)
    lstmX = dfX.values
    lstmX = lstmX.reshape(lstmX.shape[0], 1, lstmX.shape[1])
    lstmY = dfy.values
    return lstmX, lstmY


# binary encode an input pattern, return a list of binary vectors
def encode(pattern, n_unique):
    encoded = list()
    for value in pattern:
        row = [0.0 for x in range(n_unique)]
        row[value] = 1.0
        encoded.append(row)
    return encoded


def to_xy_pairs(encoded):
    X, y = list(), list()
    for i in range(1, len(encoded)):
        X.append(encoded[i - 1])
        y.append(encoded[i])
    return X, y


seq1 = [3, 0, 1, 2, 3]
seq2 = [4, 0, 1, 2, 4]
n_unique = len(set(seq1 + seq2))

seq1X, seq1Y = to_lstm_dataset(seq1, n_unique)
seq2X, seq2Y = to_lstm_dataset(seq2, n_unique)
# 输出结果
"""
[[[0. 0. 0. 1. 0.]],
 [[1. 0. 0. 0. 0.]],
 [[0. 1. 0. 0. 0.]],
 [[0. 0. 1. 0. 0.]]]
"""
print(seq1X)
"""
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]]
"""
print(seq1Y)
"""
[[[0. 0. 0. 0. 1.]]
 [[1. 0. 0. 0. 0.]]
 [[0. 1. 0. 0. 0.]]
 [[0. 0. 1. 0. 0.]]]
"""
print(seq2X)
"""
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1.]]
"""
print(seq2Y)


model = Sequential()
model.add(LSTM(20, batch_input_shape=(1, 1, 5), stateful=True))
model.add(Dense(5, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam')


for i in range(650):
    model.fit(seq1X, seq1Y, epochs=1, batch_size=1, verbose=1, shuffle=False)
    model.reset_states()
    model.fit(seq2X, seq2Y, epochs=1, batch_size=1, verbose=0, shuffle=False)
    model.reset_states()

n_batch = 1

print('Sequence 1')
result = model.predict_classes(seq1X, batch_size=n_batch, verbose=0)
model.reset_states()
for i in range(len(result)):
    print('X=%.1f y=%.1f, yhat=%.1f' % (seq1[i], seq1[i + 1], result[i]))

# 测试 LSTM对“数列2”预测
print('Sequence 2')
result = model.predict_classes(seq2X, batch_size=n_batch, verbose=0)
model.reset_states()
for i in range(len(result)):
    print('X=%.1f y=%.1f, yhat=%.1f' % (seq2[i], seq2[i + 1], result[i]))