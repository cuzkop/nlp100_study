# 56. 共参照解析
# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

import xml.etree.ElementTree as ET

tree = ET.parse("tmp/nlp.txt.xml")

representative_mentions = {}
for core in tree.iterfind("./document/coreference/coreference"):

    sentence = core.findtext('./mention[@representative="true"]/text')

    for mention in core.iterfind("./mention"):
        if mention.get("representative", "false") == "false":
            sent_id = int(mention.findtext("sentence"))
            start = int(mention.findtext("start"))
            end = int(mention.findtext("end"))

            if not (sent_id, start) in representative_mentions:
                representative_mentions[(sent_id, start)] = (end, sentence)

for sentence in tree.iterfind("./document/sentences/sentence"):
    sent_id = int(sentence.get("id"))
    org_rest = 0

    for token in sentence.iterfind("./tokens/token"):
        token_id = int(token.get("id"))

        if org_rest == 0 and (sent_id, token_id) in representative_mentions:
            (end, rep_text) = representative_mentions[(sent_id, token_id)]

            print(rep_text + '(', end='')
            org_rest = end - token_id

        # token出力
        print(token.findtext('word'), end='')

        # 置換の終わりなら閉じカッコを挿入
        if org_rest > 0:
            org_rest -= 1
            if org_rest == 0:
                print(')', end='')

        print(' ', end='')

    print()