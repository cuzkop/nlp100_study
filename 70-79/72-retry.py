# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．


import csv
import re
import sys
from collections import Counter

from nltk.stem.porter import PorterStemmer

stop_words = []
stemmer = PorterStemmer()

with open("tmp/stopword.tsv") as target:
    tsv = csv.reader(target, delimiter="\t")
    for t in tsv:
        for word in t:
            stop_words.append(word.lower())


def is_stopword(word: str) -> bool:
    return word.lower() not in stop_words

counter = Counter()
with open("tmp/sentiment.txt", mode="r", encoding="utf8", errors="ignore") as sentiment:
    for s in sentiment:
        ss = re.split(r'\s|,|\.|\(|\)|\'|/|\'|\[|\]|-', s[3:])
        # print(ss)
        f = filter(is_stopword, ss)
        xs = map(stemmer.stem, f)
        print(list(xs))
        sys.exit()
        for word in s[3:].split(" "):
            word = word.strip()
            if is_stopword(word) == True:
                continue

            word = stemmer.stem(word)
            if "\n" in word:
                word = word.strip("\n")

            if word == "!" and word == "?" and len(word) <= 1:
                continue

            counter.update([word])

features = [word for word, cnt in counter.items() if cnt >= 6]

with open("tmp/features_retry.txt", mode="w", encoding="utf8", errors="ignore") as features_file:
    features_file.write("\n".join(features))
