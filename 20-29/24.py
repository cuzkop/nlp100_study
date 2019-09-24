# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]

pattern = r"(?:File|ファイル):(.*?)\|"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE)
result = p.findall(getText())

for l in result:
    print(l)