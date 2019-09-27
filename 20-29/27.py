# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import gzip
import json
import re

def getText():
    with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
     for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            return jl["text"]

def removeEmphasis(t):
    pattern = r"(\'{2,5})(.*?)(\1)"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
    t = p.sub(r"\2", t)
    pattern = r"\[\[(?:[^|]*?\|)??([^|]*?)\]\]"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
    return p.sub(r"\1", t)
    



pattern = r"^\{\{基礎情報.*?$(.*?)^\}\}$"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
result = p.findall(getText())

pattern = r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))"
p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)

f = p.findall(result[0])

d = {}
for s in f:
    # print(removeEmphasis(s[1]))
    d[s[0]] = removeEmphasis(s[1])

print(d)
