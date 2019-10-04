# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

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
nList = []
for ls in l:
    n = []
    for d in ls:
        if d["pos"] == "名詞":
            n.append(d["surface"])
        else:
            if len(n) > 1:
                nList.append("".join(n))
            n = []
    
    if len(n) > 1:
        nList.append("".join(n))

print(set(nList))

