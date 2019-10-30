# 59. S式の解析
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

import xml.etree.ElementTree as ET
import re
import sys

tree = ET.parse("tmp/nlp.txt.xml")
pattern = r"^\((.*?)\s(.*?)\)$"
p = re.compile(pattern, re.VERBOSE + re.DOTALL)

def parse_string(s, np_list):
    match = p.match(s)
    tag = match.group(1)
    val = match.group(2)

    chunk = ""
    depth = 0
    words = []

    for c in val:

        if c == "(":
            chunk += c
            depth += 1

        elif c == ")":
            chunk += c
            depth -= 1

            if depth == 0:
                words.append(parse_string(chunk, np_list))
                chunk = ""

        else:
            if not (depth == 0 and c == ' '):
                chunk += c

    if chunk != '':
        words.append(chunk)


    result = ' '.join(words)

    if tag == 'NP':
        np_list.append(result)

    return result


for parse in tree.iterfind("./document/sentences/sentence/parse"):
    result = []
    parse_string(parse.text.strip(), result)
    print(*result, sep="\n")