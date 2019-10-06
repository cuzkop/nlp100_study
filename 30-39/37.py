# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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

lw = counter.most_common(10)
words, counts = zip(*lw)

h = np.array(counts)
w = np.array(range(0, 10))
label = np.array(words)
plt.bar(w, h, tick_label=label, align="center")
plt.show()
