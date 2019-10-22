# 52. ステミング
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

import re
from stemming.porter2 import stem

def get_sentence():
    with open("tmp/nlp.txt", "r") as nlp_file:
        pattern = r"(^.*?[\.|;|:|\?|!])\s([A-Z].*)"
        p = re.compile(pattern , re.MULTILINE + re.VERBOSE + re.DOTALL)
        for line in nlp_file:
            line = line.strip()
            m = p.match(line)
            if m:
                yield m.group(1)
                line = m.group(2)
            else:
                yield line

def get_word():
    for sentence in get_sentence():
        for s in sentence.split(" "):
            yield s


for word in get_word():
    w = word.rstrip(".,;:?!")
    print(stem(w))