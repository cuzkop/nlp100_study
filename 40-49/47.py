# 47. 機能動詞構文のマイニング
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．

# 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

# 返事をする      と に は        及ばんさと 手紙に 主人は
# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

# コーパス中で頻出する述語（サ変接続名詞+を+動詞）
# コーパス中で頻出する述語と助詞パターン

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

    def getSaRow(self):
        for i, morph in enumerate(self.morphs[0:-1]):
            if morph.pos == "名詞" and morph.pos1 == "サ変接続" and self.morphs[i + 1].pos == "助詞" and self.morphs[i + 1].surface == "を":
                return morph.surface + self.morphs[i + 1].surface

        return ""



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


with open("tmp/47_result.txt", mode='w') as f:
    for i, c in enumerate(createList()):
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

            s = ""
            for chunkSrc in chunks:
                s = chunkSrc.getSaRow()
                if len(s) > 0:
                    rm = chunkSrc
                    break
            
            if len(s) < 1:
                continue

            chunks.remove(rm)


            f.write("{}\t{}\t{}\n".format(s + verb[0].base, " ".join(ch.getMorph("助詞")[-1].surface for ch in chunks), " ".join(ch.getSurface() for ch in chunks)))


