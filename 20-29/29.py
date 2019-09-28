# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import gzip
import json
import re
import urllib.parse, urllib.request

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

# print(urllib.parse.quote(d["国旗画像"]))

url = "https://www.mediawiki.org/w/api.php?action=query&titles=File:" + urllib.parse.quote(d["国旗画像"]) + "&format=json&prop=imageinfo&iiprop=url"
header = {"User-Agent": "test"}

req = urllib.request.Request(url = url, headers=header)
result = urllib.request.urlopen(req)

json = json.loads(result.read().decode())

print(json['query']['pages'].popitem()[1]['imageinfo'][0]['url'])

