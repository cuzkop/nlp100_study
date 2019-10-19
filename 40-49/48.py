# 48. 名詞から根へのパスの抽出
# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

# 各文節は（表層形の）形態素列で表現する
# パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た

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


with open("tmp/48_result.txt", mode='w') as f:
    for i, c in enumerate(createList()):
        if i == 7: # 例問通り8行目のみ、回答は全てあり
            for chunk in c:
                if len(chunk.getMorph("名詞")) > 0:
                    f.write(chunk.getSurface())
                    
                    dst = chunk.dst
                    while True:
                        f.write(" -> " + c[dst].getSurface())
                        dst = c[dst].dst
                        if dst == -1:
                            break

                    f.write("\n")



