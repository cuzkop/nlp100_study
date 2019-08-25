# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = "パトカー"
str2 = "タクシー"
answer = ""

for s1, s2 in zip(str1, str2):
    answer = answer + s1 + s2
print(answer)

# よりスマートな書き方
print(''.join(s1 + s2 for s1, s2 in zip(str1, str2)))