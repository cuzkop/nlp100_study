# 45. 動詞の格パターンの抽出
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

# 動詞を含む文節において，最左の動詞の基本形を述語とする
# 述語に係る助詞を格とする
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

# 始める  で
# 見る    は を
# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語と格パターンの組み合わせ
# 「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

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


with open("tmp/45_result.txt", mode='w') as f:
    for c in createList():
        for chunk in c:
            verb = chunk.getMorph("動詞")

            if len(verb) < 1:
                continue

            affects = []
            for src in chunk.srcs:
                s = c[src].getMorph("助詞")
                if len(s) < 1:
                    continue

                if len(s) > 1:
                    case = c[src].getMorph("助詞", "格助詞")
                    if len(case) > 0:
                        s = case

                if len(s) > 0:
                    affects.append(s[-1])

            if len(affects) < 1:
                continue

            f.write("{}\t{}\n".format(verb[0].base, " ".join(sorted(a.surface for a in affects))))


