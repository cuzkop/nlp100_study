# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import MeCab

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
nDict = {}
for ls in l:
    for d in ls:
        if d["surface"] not in nDict:
            nDict[d["surface"]] = 1
        else:
            nDict[d["surface"]] = nDict[d["surface"]] + 1

sortedDict = sorted(nDict.items(), key=lambda x:x[1])

for s in reversed(sortedDict):
    print(s)


