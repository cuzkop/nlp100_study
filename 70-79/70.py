# 第8章: 機械学習
# 本章では，Bo Pang氏とLillian Lee氏が公開している
# Movie Review Dataのsentence polarity dataset v1.0を用い，
# 文を肯定的（ポジティブ）もしくは否定的（ネガティブ）に分類するタスク（極性分析）に取り組む．

# 70. データの入手・整形
# 文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

# 1.rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
# 2.rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
# 3.上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
# sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

import random


def add_list(filename, pos=False, neg=False):
    result = []
    with open("tmp/rt-polaritydata/{}".format(filename), encoding="utf8", errors="ignore") as polarity:
        if pos == True:
            result.extend(["+1 {}".format(sentence.strip()) for sentence in polarity])
        if neg == True:
            result.extend(["-1 {}".format(sentence.strip()) for sentence in polarity])

    return result

polarities = add_list("rt-polarity.pos", pos=True)
polarities.extend(add_list("rt-polarity.pos", neg=True))


random.shuffle(polarities)
