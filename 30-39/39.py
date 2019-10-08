# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import MeCab
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib

with open("tmp/neko.txt", "r") as f, open("tmp/neko.txt.mecab", "w") as mf:
    m = MeCab.Tagger()
    mf.write(m.parse(f.read()))

def createList():
    with open("tmp/neko.txt.mecab", "r") as mf:
        l = []
        for m in mf:
            word = m.split("\t")
            if len(word) < 2:
                continue
            exp = word[1].split(",")
            d = {"surface" : word[0], "base" : exp[6], "pos" : exp[0], "pos1" : exp[1]}
            l.append(d)
            if exp[1] == "句点":
                yield l
                l = []


l = createList()

counter = Counter()
for ls in l:
    counter.update([d["surface"] for d in ls])

lw = counter.most_common()
words, counts = zip(*lw)

plt.xscale("log")
plt.yscale("log")

x = range(1, len(words)+1)
y = counts

plt.scatter(x, y)
plt.show()
