# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]


pattern = r"^\{\{基礎情報.*?$(.*?)^\}\}$"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
result = p.findall(getText())

pattern = r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)

f = p.findall(result[0])

d = {}
for s in f:
    d[s[0]] = s[1]

print(d)
