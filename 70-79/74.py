# 74. 予測
# 73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．

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

def hypothesis(x_train: list, theta: list):
    return 1.0 / (1.0 + np.exp(-x_train.dot(theta)))


feature_dict = load_feature()

theta = np.load("tmp/theta.npy")

argv = sys.argv
sentence = str(argv[1])

x_test = extract_feature(sentence, feature_dict)

h = hypothesis(x_test, theta)
if h > 0.5:
    print('label:+1 ({})'.format(h))
else:
    print('label:-1 ({})'.format(1 - h))