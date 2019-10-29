# 58. タプルの抽出
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

# 述語: nsubj関係とdobj関係の子（dependant）を持つ単語
# 主語: 述語からnsubj関係にある子（dependent）
# 目的語: 述語からdobj関係にある子（dependent）

import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")

for sentence in tree.iterfind("./document/sentences/sentence"):
    sentence_id = int(sentence.get("id"))