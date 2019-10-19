# 49. 名詞間の係り受けパスの抽出
# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

# 問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
# 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
# また，係り受けパスの形状は，以下の2通りが考えられる．

# 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
# 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
# 例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# Xは | Yで -> 始めて -> 人間という -> ものを | 見た
# Xは | Yという -> ものを | 見た
# Xは | Yを | 見た
# Xで -> 始めて -> Y
# Xで -> 始めて -> 人間という -> Y
# Xという -> Y


import CaboCha
import pydot_ng as pydot
import sys

with open("tmp/neko.txt") as read_file, open("tmp/neko.txt.cabocha", mode='w') as write_file:
    cabocha = CaboCha.Parser()
    for l in read_file:
        write_file.write(
            cabocha.parse(l).toString(CaboCha.FORMAT_LATTICE)
        )

class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]".format(self.surface, self.base, self.pos, self.pos1)

class Chunk:

    def __init__(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []

    def __str__(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return "{} 係り先: dst[{}]".format(surface, self.dst)

    def getSurface(self):
        surface = ""
        for morph in self.morphs:
            surface += morph.surface
        return surface

    def getPos(self, pos):
        for morph in self.morphs:
            if morph.pos == pos:
                return True

        return False

    def getMorph(self, pos, pos1=''):
        if len(pos1) > 0:
            return [m for m in self.morphs if (m.pos == pos) and (m.pos1 == pos1)]
        else:
            return [m for m in self.morphs if m.pos == pos]

    def changeNoun(self, s, dst=False):
        result = ""
        for m in self.morphs:
            if m.pos != "記号":
                if m.pos == "名詞":
                    result += s
                    if dst:
                        return result
                    s = ""
                else:
                    result += m.surface

        return result



def createList():
    with open("tmp/neko.txt.cabocha", "r") as mf:

        chunks = {}
        i = -1

        for l in mf:
            if l == "EOS\n":
                if len(chunks) > 0:
                    sortedDict = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sortedDict))[1]
                    chunks.clear()
                else:
                    yield []

            elif l[0] == "*":
                row = l.split(" ")
                i = int(row[1])
                dst = int(row[2].rstrip("D"))

                if i not in chunks:
                    chunks[i] = Chunk()

                chunks[i].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(i)

            else:
                c = l.split("\t")
                s = c[1].split(",")

                chunks[i].morphs.append(Morph(c[0], s[6], s[0], s[1]))

        raise StopIteration


with open("tmp/49_result.txt", mode='w') as f:
    for i, c in enumerate(createList()):
        if i == 7: # 例問通り8行目のみ 解答は重すぎて上げられず
            nouns = []
            for i, chunk in enumerate(c):
                if len(chunk.getMorph("名詞")) < 1:
                    continue
                nouns.append(i)

            if len(nouns) < 2:
                continue

            for i, nounsIndex in enumerate(nouns[:-1]):
                for yIndex in nouns[i+1:]:
                    y = False
                    index = -1
                    xRoute = set()
                    dst = c[nounsIndex].dst
                    
                    while True:
                        if dst == yIndex:
                            y = True
                            break
                        xRoute.add(dst)
                        dst = c[dst].dst
                        if dst == -1:
                            break

                    if not y:
                        dst = c[yIndex].dst
                        while True:
                            if dst in xRoute:
                                index = dst
                                break
                            else:
                                dst = c[dst].dst
                            if dst == -1:
                                break

                    if index == -1:
                        f.write(c[nounsIndex].changeNoun("X"))
                        dst = c[nounsIndex].dst
                        while dst != -1:
                            if dst == yIndex:
                                f.write(" -> " + c[dst].changeNoun('Y', True))
                                break
                            else:
                                f.write(" -> " + c[dst].getSurface())
                            dst = c[dst].dst
                        
                        f.write("\n")

                    else:
                        f.write(c[nounsIndex].changeNoun("X"))
                        dst = c[nounsIndex].dst
                        while dst != index:
                            f.write(" -> " + c[dst].getSurface())
                            dst = c[dst].dst
                        
                        f.write(" | ")

                        f.write(c[yIndex].changeNoun("Y"))
                        dst = c[yIndex].dst
                        while dst != index:
                            f.write(" -> " + c[dst].getSurface())
                            dst = c[dst].dst
                        f.write(" | ")

                        f.write(c[index].getSurface())
                        f.write("\n")
