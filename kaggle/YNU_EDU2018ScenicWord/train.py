#coding:utf-8

import pandas as pd 
import numpy as np
import jieba


train = pd.read_csv('/Users/zhangguxin/Downloads/zgx/kaggle/YNU_EDU2018ScenicWord/train_first.csv', sep=',')
test = pd.read_csv('/Users/zhangguxin/Downloads/zgx/kaggle/YNU_EDU2018ScenicWord/predict_first.csv', sep=',')

train.columns = ['id', 'discuss', 'score']
test.columns = ['id', 'discuss']

train['is_train'] = 1
test['is_train'] = 0

data = pd.concat([train, test], axis=0, ignore_index=True)

#1.分词 tokenize

data['discuss_cut'] = data['discuss'].map(lambda x: [i for i in jieba.cut(x)])

data['discuss_cut'] = data['discuss'].map(jieba.lcut)


#2.去停用词


#2.1.wordcount

with open('/Users/zhangguxin/Downloads/zgx/kaggle/YNU_EDU2018ScenicWord/train_first.csv', mode='r', encoding='utf-8') as f:
    word_list = {}
    for line in f.readlines():
        for word in jieba.lcut(line.strip().split(',')[1]):
            if word in word_list.keys():
                word_list[word] += 1
            else:
                word_list[word] = 1


with open('/Users/zhangguxin/Downloads/zgx/kaggle/YNU_EDU2018ScenicWord/predict_first.csv', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        for word in jieba.lcut(line.strip().split(',')[1]):
            if word in word_list.keys():
                word_list[word] += 1
            else:
                word_list[word] = 1


word_list_sorted = sorted(word_list.items(), key=lambda item: item[1], reverse=True)

word_list_dict = pd.DataFrame.from_dict(word_list_sorted)
word_list_dict.columns = ['word', 'count']


stopwords = []
with open('/Users/zhangguxin/Downloads/test2/07_text_analytics/stopword.txt') as f:
    for line in f.readlines():
        stopwords.append(line.strip().split(' ')[0])


for k, v in word_list_dict.items():
	if k in stopwords:
		del word_list_dict[k]


def filter_stop_words(text):
	words = [w for w in text if w not in stopwords]
	return ' '.join(words)


data['clean_discuss'] = data['discuss_cut'].map(filter_stop_words)

#3.词性标注（某些分类某种类型词会对分类起很大作用，比如名词对新闻分类、形容词对情感分析）


#4.特征提取（tf-idf, bow, w2v, countVectorizer等）

def bag_of_words():
	pass

def tf_idf():
	pass

def countVectorizer():
	pass

from sklearn.feature_extraction.text import CountVectorizer 

vectorizer = CountVectorizer(max_features = 5000)

train_data_features = vectorizer.fit_transform(data['clean_discuss']).toarray()

train_x = train_data_features[0:100000,:]

train_y = np.array(data[data['is_train']==1]['score'])

test = train_data_features[100000:, :]

def word2vec
	pass

#https://stackoverflow.com/questions/47028943/gensim-keyerror-word-quick-not-in-vocabulary

from gensim.models.word2vec import Word2Vec

NUM_FEATURES = 300 #word vector dimensionality
MIN_WORD_COUNT = 1 #minimun word count
NUM_WORKERS = 4 # number of threads to run in parallel
CONTEXT = 10 #context window size
DOWNSAMPLING = 1E-3 #downsample setting for frequent words

sentences = []

for i in data['discuss_cut'][0: 1000]:
    sentences.append(i)

model = Word2Vec(
	sentences, 
	workers = NUM_WORKERS,
	size = NUM_FEATURES,
	min_count = MIN_WORD_COUNT,
	window = CONTEXT,
	sample = DOWNSAMPLING
	)

model.most_similar('很好')


def lstm():
	pass

#5.构造分类器


import xgboost as xgb 













