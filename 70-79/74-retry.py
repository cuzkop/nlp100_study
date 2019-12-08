# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

import csv
import sys
import random
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import scipy.stats
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score

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
            y_train[i] = -1
        
        for word in s.split(" "):
            if is_stopword(word):
                continue

            if word in feature_dict:
                x_train[i][feature_dict[word]] = 1


    return x_train, y_train

with open("tmp/features_retry.txt") as features:
    feature_dict = create_feature_dict(features)


with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:

    # max_score = 0
    # SearchMethod = 0
    # LR_grid = {LogisticRegression(): {"C": [10 ** i for i in range(-5, 6)],
    #                                 "random_state": [i for i in range(0, 101)]}}
    # LR_random = {LogisticRegression(): {"C": scipy.stats.uniform(0.00001, 1000),
    #                                     "random_state": scipy.stats.randint(0, 100)}}

    x, y = create_train(sentiment.readlines(), feature_dict)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
    print(y_train)
    print(y_test)

    # for model, param in LR_grid.items():
    #     clf = GridSearchCV(model, param)
    #     clf.fit(X_train, y_train)
    #     pred_y = clf.predict(X_test)
    #     score = f1_score(y_test, pred_y, average="micro")

    #     if max_score < score:
    #         max_score = score
    #         best_param = clf.best_params_
    #         best_model = model.__class__.__name__


    # for model, param in LR_random.items():
    #     clf =RandomizedSearchCV(model, param)
    #     clf.fit(X_train, y_train)
    #     pred_y = clf.predict(X_test)
    #     score = f1_score(y_test, pred_y, average="micro")

    #     if max_score < score:
    #         SearchMethod = 1
    #         max_score = score
    #         best_param = clf.best_params_
    #         best_model = model.__class__.__name__

    
    # if SearchMethod == 0:
    #     print("サーチ方法:グリッドサーチ")
    # else:
    #     print("サーチ方法:ランダムサーチ")
    # print("ベストスコア:{}".format(max_score))
    # print("モデル:{}".format(best_model))
    # print("パラメーター:{}".format(best_param))

    # #ハイパーパラメータを調整しない場合との比較
    model = LogisticRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print("")
    print("デフォルトスコア:", score)

    # for c in costs:
    # lr = LogisticRegression(solver="sag", max_iter=10000, C=5)
    # lr.fit(X_train, y_train)
    # y_train_pred = lr.predict(X_train)
    # y_test_pred = lr.predict(X_test)
    # print(y_test_pred[:10])
    # print(y_test[:10])
    # print(accuracy_score(y_train, y_train_pred), accuracy_score(y_test, y_test_pred))
    # print(len(lr.coef_[0]))