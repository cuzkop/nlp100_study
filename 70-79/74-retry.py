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
lr = LogisticRegression(solver='sag', random_state=1234)

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

texts = [
    "simplistic , silly and tedious . ",
    "it's so laddish and juvenile , only teenage boys could possibly find it funny . ",
    "exploitative and largely devoid of the depth or sophistication that would make watching such a graphic treatment of the crimes bearable . ",
    "effective but too-tepid biopic",
    "if you sometimes like to go to the movies to have fun , wasabi is a good place to start . ",
    "emerges as something rare , an issue movie that's so honest and keenly observed that it doesn't feel like one . ",
    "with a cast that includes some of the top actors working in independent film , lovely & amazing involves us because it is so incisive , so bleakly amusing about how we go about our lives . "
]

for text in texts:
    text_list = re.split(r'\s|,|\.|\(|\)|\'|/|\'|\[|\]|-', text[3:])
    filtered_list = filter(is_stopword, text_list)
    stems = list(map(stemmer.stem, filtered_list))
    x_test = ' '.join(stems)
    x = cv.transform([x_test])
    y_test_pred = lr.predict(x)
    pr = lr.predict_proba(x)

    print(x_test)
    print('予測：{} 確率：{}\n'.format('+1' if y_test_pred[0] == 1 else '-1', pr[0][0] if y_test_pred[0] == 0 else pr[0][1]))

    # counter.update([' '.join(stems)])