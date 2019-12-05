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

with open("tmp/features_retry.txt") as features:
    feature_list = features.read().splitlines()



with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:
    train_y = [1 if s[:2] == "+1" else 0 for s in sentiment]
    
    # data_x, data_y = create_datasets(list(sentiment), dict_features)

print('学習率：{}\t学習繰り返し数：{}'.format(6.0, 1000))
theta = learn(data_x, data_y, alpha=6.0, count=1000)