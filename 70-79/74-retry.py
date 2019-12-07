# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

import csv
import sys
import random
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

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
    x, y = create_train(sentiment.readlines(), feature_dict)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

    lr = LogisticRegression(solver="sag", max_iter=10000, C=0.2)
    lr.fit(X_train, y_train)
    y_train_pred = lr.predict(X_train)
    y_test_pred = lr.predict(X_test)
    print(accuracy_score(y_train, y_train_pred), accuracy_score(y_test, y_test_pred))
    print(len(lr.coef_[0]))

# lr = LogisticRegression(n_jobs=-1)
# lr.fit(x_train, y_train)


# with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:
#     x_test, _ = create_train(sentiment.readlines(), feature_dict)

# x_test, _ = create_train(sentence, feature_dict)

# result = lr.predict(x_test)
# for r in result:
#     print(r)
# print(x_test)