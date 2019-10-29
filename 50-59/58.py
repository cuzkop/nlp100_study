# 58. タプルの抽出
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

# 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# 主語: 述語からnsubj関係にある子（dependent）
# 目的語: 述語からdobj関係にある子（dependent）

import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")

dep_text = {}
dep_nsubj = {}
dep_dobj = {}

for sentence in tree.iterfind("./document/sentences/sentence"):
    sentence_id = int(sentence.get("id"))
    for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/dep"):
        if dep.get("type") == "dobj" or dep.get("type") == "nsubj":
            dep_text[dep.find("./governor").get("idx")] = dep.find("./governor").text

            if dep.get("type") == "dobj":
                dep_dobj[dep.find("./governor").get("idx")] = dep.find("./dependent").text

            if dep.get("type") == "nsubj":
                dep_nsubj[dep.find("./governor").get("idx")] = dep.find("./dependent").text
            
    for idx, txt in dep_text.items():
        n = dep_nsubj.get(idx)
        d = dep_dobj.get(idx)
        if d != None and n != None:
            print("{}\t{}\t{}".format(n, txt, d))