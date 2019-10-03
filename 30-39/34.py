# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

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
for ls in l:
    for i, d in enumerate(ls):
        if d["surface"] == "の" and ls[i - 1]["pos"] == "名詞" and ls[i + 1]["pos"] == "名詞":
            print(ls[i - 1]["surface"] + d["surface"] + ls[i + 1]["surface"])
