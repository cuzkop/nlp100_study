# 57. 係り受け解析
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

import pydot_ng as pydot
import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")

for sentence in tree.iterfind("./document/sentences/sentence"):
    sentence_id = int(sentence.get("id"))
    if sentence_id == 3:
        break

    edges = []

    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):

        if dep.get("type") == "punct":
            continue

        governor = dep.find("./governor")
        dependent = dep.find("./dependent")
        edges.append(((governor.get("idx"), governor.text), (dependent.get("idx"), dependent.text)))

    if len(edges) < 1:
        continue

    graph = pydot.Dot(graph_type="graph")
    for edge in edges:
        id1, id2 = str(edge[0][0]), str(edge[1][0])
        label1, label2 = str(edge[0][1]), str(edge[1][1])

        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        graph.add_edge(pydot.Edge(id1, id2))
        graph.write_png("tmp/graph_nlp{}.png".format(sentence_id))