# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．


import csv
import re
import sys
from collections import Counter

from nltk.stem.porter import PorterStemmer
import nltk

from nltk.corpus import stopwords

stop_words = []
stemmer = PorterStemmer()
stop_words = ['a', 'about', 'all', 'an', 'and', 'any', 'are', 'as', \
            'at', 'be', 'been', 'but', 'by', 'can', 'could', 'do', \
            'does', 'for', 'from', 'has', 'have', 'he', 'her', 'his', \
            'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'made', \
            'make', 'may', 'me', 'my', 'no', 'not', 'of', 'on', 'one', \
            'or', 'out', 'she', 'should', 'so', 'some', 'than', 'that', \
            'the', 'their', 'them', 'there', 'then', 'they', 'this', \
            'those', 'to', 'too', 'us', 'was', 'we', 'what', 'when',\
            'which', 'who', 'with', 'would', 'you', 'your', ''
        ]


def is_stopword(word: str) -> bool:
    if word == '' or len(word) <= 2:
        return False

    if re.match(r'^[-=!@#$%^&*()_+|;";,.<>/?]+$', word): #記号等だったらFalse
        return False

    return word.lower() not in stop_words

counter = Counter()
with open("tmp/sentiment3.txt", mode="r", encoding="utf8", errors="ignore") as sentiment:
    for s in sentiment:
        sentiment_list = re.split(r'\s|,|\.|\(|\)|\'|/|\'|\[|\]|-', s[3:])
        filtered_list = filter(is_stopword, sentiment_list)
        stems = list(map(stemmer.stem, filtered_list))
        stems.insert(0, s[:2])

        counter.update([' '.join(stems)])

features = [word for word, cnt in counter.items()]

with open("tmp/features_retry3.txt", mode="w", encoding="utf8", errors="ignore") as features_file:
    features_file.write("\n".join(features))
