# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]


pattern = r"^(={2,})\s*(.+?)\s*\1.*$"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE)
result = p.findall(getText())
for l in result:
    print(l[1], len(l[0])-1)
