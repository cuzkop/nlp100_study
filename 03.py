# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(",", "").replace(".", "")
answer = []
for s in str.split(" "):
    answer.append(len(s))

print(answer)

# こっちの方がいいらしい

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
import re
print(list(len(m) for m in re.findall('[a-zA-Z]+', s)))