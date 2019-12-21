# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．


import csv
import re
import sys
from collections import Counter

import joblib
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

stemmer = PorterStemmer()
cv = CountVectorizer(encoding='utf-8')
lr = LogisticRegression(solver='sag', random_state=1500, C=10000)

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


with open("tmp/features_retry3.txt") as features:
    x = []
    y = []
    for f in features:
        x.append(f[3:].strip())
        y.append(1.0 if f[0] == "+" else 0.0)


x_cv = cv.fit_transform(x)
lr.fit(x_cv, y)
joblib.dump(cv, 'tmp/cv73-retry.learn')
joblib.dump(lr, 'tmp/lr73-retry.learn')

texts = [\
    'perhaps the best sports movie i''ve ever seen.', \
    'i had more fun watching spy than i had with most of the big summer movies.', \
    'vividly conveys the shadow side of the 30-year friendship between two english women.', \
    'an excruciating demonstration of the unsalvageability of a movie saddled with an amateurish screenplay.', \
    'sadly , hewitt''s forte is leaning forward while wearing low-cut gowns , not making snappy comebacks.', \
    'since lee is a sentimentalist , the film is more worshipful than your random e ! true hollywood story.', \
    "simplistic , silly and tedious . ", \
    "it's so laddish and juvenile , only teenage boys could possibly find it funny . ", \
    "exploitative and largely devoid of the depth or sophistication that would make watching such a graphic treatment of the crimes bearable . ", \
    

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
