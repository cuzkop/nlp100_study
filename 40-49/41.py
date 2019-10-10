# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．


import CaboCha
import re
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


def createList():
    with open("tmp/neko.txt.cabocha", "r") as mf:

        chunks = {}
        i = -1

        for l in mf:
            if l == "EOS\n":
                if len(chunks) > 0:
                    sorted_tuple = sorted(chunks.items(), key=lambda x: x[0])
                    yield list(zip(*sorted_tuple))[1]
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




createList()

for i, m in enumerate(createList(), 1):
    if i == 8:
        for morph in m:
            print(morph)
        break