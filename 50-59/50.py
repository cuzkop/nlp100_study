# 第6章: 英語テキストの処理
# 英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

# 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

import re

with open("tmp/nlp.txt", "r") as nlp_file:
    pattern = r"(^.*?[\.|;|:|\?|!])\s([A-Z].*)"
    p = re.compile(pattern , re.MULTILINE + re.VERBOSE + re.DOTALL)
    for line in nlp_file:
        line = line.strip()
        m = p.match(line)
        if m:
            print(m.group(1))
            line = m.group(2)
        else:
            print(line)

