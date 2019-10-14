# 46. 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

# 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

# 始める  で      ここで
# 見る    は を   吾輩は ものを

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


with open("tmp/46_result.txt", mode='w') as f:
    for i, c in enumerate(createList()):
        if i == 7: # 例問通り8行目のみ、回答は全てあり
            for chunk in c:
                verb = chunk.getMorph("動詞")

                if len(verb) < 1:
                    continue

                chunks = []
                for src in chunk.srcs:
                    s = c[src].getMorph("助詞")
                    if len(s) < 1:
                        continue

                    if len(s) > 1:
                        case = c[src].getMorph("助詞", "格助詞")
                        if len(case) > 0:
                            s = case

                    if len(s) > 0:
                        chunks.append(c[src])

                if len(chunks) < 1:
                    continue

                f.write("{}\t{}\t{}\n".format(verb[0].base, " ".join(ch.getMorph("助詞")[-1].surface for ch in chunks), " ".join(ch.getSurface() for ch in chunks)))


