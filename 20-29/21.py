# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]


pattern = r"^(.*\[\[Category:.*\]\].*)$"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE)
result = p.findall(getText())
print(result)
