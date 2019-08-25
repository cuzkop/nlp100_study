# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

str = "stressed"
print(str[::-1])

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

str = "パタトクカシーー"
print(str[::2])

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = "パトカー"
str2 = "タクシー"
answer = ""

for s1, s2 in zip(str1, str2):
    answer = answer + s1 + s2
print(answer)

# よりスマートな書き方
print(''.join(s1 + s2 for s1, s2 in zip(str1,str2)))