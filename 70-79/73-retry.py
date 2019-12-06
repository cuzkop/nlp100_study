# 73. 学習
# 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

import csv
import sys
import random
from collections import Counter
from sklearn.linear_model import LogisticRegression

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

def create_feature_dict(features):
    feature_dict = {}
    for i, f in enumerate(features):
        feature_dict[f.strip()] = i

    return feature_dict

def create_train(sentiment, feature_dict):
    x_train = np.zeros([len(sentiment), len(feature_dict)], dtype=np.float64)
    y_train = np.zeros(len(sentiment), dtype=np.float64)

    for i, s in enumerate(sentiment):
        if s[:2] == "+1":
            y_train[i] = 1
        else:
            y_train[i] = 0
        
        for word in s.split(" "):
            if is_stopword(word):
                continue

            if word in feature_dict:
                x_train[i][feature_dict[word]] = 1


    return x_train, y_train
        
    

with open("tmp/features_retry.txt") as features:
    feature_dict = create_feature_dict(features)



with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:
    x_train, y_train = create_train(sentiment.readlines(), feature_dict)

lr = LogisticRegression()
lr.fit(x_train, y_train)
