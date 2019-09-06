# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sentenceList = sentence.split(" ")

l = []

for s in sentenceList:
    if len(s) > 4:
        s = list(s)
        rand_s = s[1:-1]
        random.shuffle(rand_s)
        s = s[0] + "".join(rand_s) + s[-1]

    l.append(s)

print(" ".join(l))