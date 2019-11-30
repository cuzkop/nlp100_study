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

def get_dict_feature() -> dict:
    with open("tmp/features_retry.txt", mode="r", encoding="utf8") as feature:
        return {f.strip(): i for i, f in enumerate(feature, start=1)}

def create_datasets(sentiment: list, dict_features: dict):
    data_x = np.zeros([len(sentiment), len(dict_features) + 1], dtype=np.float64)
    print(data_x)

dict_features = get_dict_feature()

with open("tmp/sentiment.txt", mode="r", encoding="utf8") as sentiment:
    data_x, data_y = create_datasets(list(sentiment), dict_features)