# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

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

    pattern = r"\[\[(?:[^|]*?\|)*?([^|]*?)\]\]"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
    t = p.sub(r"\1", t)

    pattern = r"\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
    t = p.sub(r"\1", t)

    pattern = r"\[http://\/\/(?:[^\s]*?\s)?([^]]*?)\]"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)
    t = p.sub(r"\1", t)

    pattern = r"<\/?[br|ref][^>]*?>"
    p = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)

    return p.sub("", t)
    



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
