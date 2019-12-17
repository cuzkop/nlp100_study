# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．


import csv
import re
import sys
from collections import Counter

from nltk.stem.porter import PorterStemmer
import nltk

from nltk.corpus import stopwords

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer


stop_words = []
stemmer = PorterStemmer()
stop_words = frozenset(stopwords.words('english'))
cv = CountVectorizer(encoding='utf-8')
lr = LogisticRegression(solver='sag')

def is_stopword(word: str) -> bool:
    if word == '' or len(word) <= 2:
        return False

    if re.match(r'^[-=!@#$%^&*()_+|;";,.<>/?]+$', word): #記号等だったらFalse
        return False

    return word.lower() not in stop_words


with open("tmp/features_retry.txt") as features:
    x = []
    y = []
    for f in features:
        x.append(f[3:].strip())
        y.append(1.0 if f[0] == "+" else 0.0)

x_cv = cv.fit_transform(x)
lr.fit(x_cv, y)

