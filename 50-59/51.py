# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

import re
import sys

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

for sentence in get_sentence():
    for s in sentence.split(" "):
        print(s)
    
    print("\n")