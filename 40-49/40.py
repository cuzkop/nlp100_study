# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．


import CaboCha

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

def createList():
    with open("tmp/neko.txt.cabocha", "r") as mf:
        l = []
        for m in mf:
            if m == "EOS\n":
                yield l
                l = []

            else:
                if m[0] == "*":
                    continue

                c = m.split("\t")
                s = c[1].split(",")
                l.append(Morph(c[0], s[6], s[0], s[1]))

        raise StopIteration




createList()

for i, m in enumerate(createList(), 1):
    if i == 3:
        for morph in m:
            print(morph)
        break