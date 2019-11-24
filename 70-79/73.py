# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

import csv
import sys
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

def load_feature() -> dict:
    with open("tmp/features.txt", mode="r", encoding="utf8", errors="ignore") as feature:
        return {f.strip(): i for i, f in enumerate(feature, start=1)}

def create_train_data(sentiments: list, feature_dict: dict) -> list:
    train_x = np.zeros([len(sentiments), len(feature_dict) + 1], dtype=np.float64)
    train_y = np.zeros(len(sentiments), dtype=np.float64)

    for i, sentiment in enumerate(sentiments):
        train_x[i] = extract_feature(sentiment[3:], feature_dict)
        
        if sentiment[0:2] == "+1":
            train_y[i] = 1

    return train_x, train_y

def extract_feature(data: str, feature_dict: dict) -> list:
    train_x = np.zeros(len(feature_dict) + 1, dtype=np.float64)
    train_x[0] = 1

    for word in data.split(' '):
        word = word.strip()
        
        if is_stopword(word):
            continue

        word = stem(word)

        try:
            train_x[feature_dict[word]] = 1
        except:
            pass

    return train_x

def learn(x_train: list, y_train: list, alpha: float, cnt: int):
    theta = np.zeros(x_train.shape[1])
    c = cost(x_train, y_train, theta)

    for i in range(1, cnt + 1):

        grad = gradient(x_train, y_train, theta)
        theta -= alpha * grad

    c = cost(x_train, y_train, theta)
    e = np.max(np.absolute(alpha * grad))
    return theta

def gradient(x_train: list, y_train: list, theta: list) -> list:
    y_size = y_train.size
    hypo = hypothesis(x_train, theta)
    grad = 1 / y_size * (hypo - y_train).dot(x_train)
    return grad

def cost(x_train: list, y_train: list, theta: list) -> float: 
    y_size = y_train.size
    hypo = hypothesis(x_train, theta)
    j = 1 / y_size * np.sum(-y_train * np.log(hypo) - (np.ones(y_size) - y_train) * np.log(np.ones(y_size) - hypo))
    return j

def hypothesis(x_train: list, theta: list):
    return 1.0 / (1.0 + np.exp(-x_train.dot(theta)))


feature_dict = load_feature()

with open("tmp/sentiment.txt", mode="r", encoding="utf8", errors="ignore") as sentiment:
    x_train, y_train = create_train_data(list(sentiment), feature_dict)

theta = learn(x_train, y_train, 6.0, 1000)
np.save("tmp/theta.npy", theta)