# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

strx = "paraparaparadise"
stry = "paragraph"

def n_gram(n, s):
    rt = []
    for i in range(len(s) - n + 1):
        rt.append(s[i:i+n])
    return rt

setx = set(n_gram(2, strx))
sety = set(n_gram(2, stry))

print(setx.union(sety)) #和集合
print(setx.intersection(sety)) #積集合
print(setx.difference(sety)) #差集合
print("se" in setx)
print("se" in sety)