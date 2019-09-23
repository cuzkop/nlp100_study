# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]


pattern = r"^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE)
result = p.findall(getText())
print(result)
