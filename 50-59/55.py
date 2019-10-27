# 55. 固有表現抽出
# 入力文中の人名をすべて抜き出せ．

import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")

for t in tree.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]'):
    print(t.findtext("word"))