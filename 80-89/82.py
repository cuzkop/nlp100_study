# 82. 文脈の抽出
# 81で作成したコーパス中に出現するすべての単語tに関して，単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．ただし，文脈語の定義は次の通りとする．

# ある単語tの前後d単語を文脈語cとして抽出する（ただし，文脈語に単語tそのものは含まない）
# 単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．

import random

cnt = 0
with open('tmp/81.txt', 'r') as file81:
    for l in file81:
        sentence_list = list(l.split())
        if len(sentence_list) <= 1:
            continue

        for i, word in enumerate(sentence_list):
            width = random.randint(1,5)
            comtext = []
            start = i-width if i-width >= 0 else 0
            end = i+width if i+width <= len(sentence_list) else len(sentence_list)

            for j in range(start, end+1):
                if j == i:
                    continue
                if j < len(sentence_list):
                    print("{}\t{}".format(word, sentence_list[j]))
