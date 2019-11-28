# 71. ストップワード
# 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

# https://docs.oracle.com/cd/E16338_01/text.112/b61357/astopsup.htm
# oracleの英語のデフォルトストップリストより

import csv

stop_words = []

with open("tmp/stopword.tsv") as target:
    tsv = csv.reader(target, delimiter="\t")
    for t in tsv:
        for word in t:
            stop_words.append(word.lower())


def is_stopword(word: str) -> bool:
    return word.lower() in stop_words

assert is_stopword("a")
assert is_stopword("A")
assert is_stopword("mrs")
assert not is_stopword("b")
