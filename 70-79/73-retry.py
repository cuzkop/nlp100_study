# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

import csv
import sys
import random
from collections import Counter

import numpy as np

from stemming.porter2 import stem

stop_words = []

with open("tmp/stopword.tsv") as target:
    tsv = csv.reader(target, delimiter="\t")
    for t in tsv:
        for word in t:
            stop_words.append(word.lower())


def is_stopword(word: str) -> bool:
    return word.lower() in stop_words

def get_dict_feature() -> dict:
    with open("tmp/features_retry.txt", mode="r", encoding="utf8") as feature:
        return {f.strip(): i for i, f in enumerate(feature, start=1)}

def create_datasets(sentiment: list, dict_features: dict):
    data_x = np.zeros([len(sentiment), len(dict_features) + 1], dtype=np.float64)
    data_y = np.zeros(len(sentiment), dtype=np.float64)
    
    for i, s in enumerate(sentiment):
        data_x[i] = extract_features(s[3:], dict_features)

        if s[0:2] == "+1":
            data_y[i] = 1
        
        
    return data_x, data_y

def extract_features(sentiment, dict_features):
    data_one_x = np.zeros(len(dict_features) + 1, dtype=np.float64)
    data_one_x[0] = 1

    for s in sentiment.split(" "):
        s = s.strip()

        if is_stopword(s) == True:
            continue

        s = stem(s)

        try:
            data_one_x[dict_features[s]] = 1
        except:
            pass

    return data_one_x

def learn(data_x, data_y, alpha, count):
    w = random.randrange(len(data_y) + 1)
    theta = np.zeros(data_x.shape[1])
    c = cost(data_x, theta, data_y, w)

    print('\t学習開始\tcost：{}'.format(c))
    
    for i in range(count):
        grad = gradient(data_x, theta, data_y)
        theta -= alpha * grad
        print(grad)
        sys.exit()

def cost(data_x, theta, data_y, w):
    m = data_y.size
    h = hypothesis(data_x, theta, w)
    j = 1 / m * np.sum(-data_y * np.log(h) - (np.ones(m) - data_y) * np.log(np.ones(m) - h))

    return j

def hypothesis(data_x, theta, w):
    return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))
    # return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))

def gradient(data_x, theta, data_y):
    m = data_y.size
    h = hypothesis(data_x, theta, 1)
    s = h - data_y
    p, ms = 0, 0
    for ss in s:
        if ss == 0.5:
            p += 1
        else:
            ms += 1
    
    print(p, ms)
    sys.exit()
    grad = 1 / m * (h - data_y).dot(data_x)

    return grad

dict_features = get_dict_feature()

with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:
    data_x, data_y = create_datasets(list(sentiment), dict_features)

print('学習率：{}\t学習繰り返し数：{}'.format(6.0, 1000))
theta = learn(data_x, data_y, alpha=6.0, count=1000)