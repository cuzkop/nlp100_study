# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from itertools import groupby
with open("tmp/hightemp.txt", "r") as f:
    files = f.readlines()

prefs = []
for l in files:
    prefs.append(l.split("\t")[0])

prefs.sort()
prefLst = []

for n, i in groupby(prefs):
    prefLst.append((len(list(i)), n))
    
prefLst.sort(key=lambda x:x[0], reverse=True)

for k in prefLst:
    print(k[1])

# cut -f 1 tmp/hightemp.txt | sort | uniq -c | sort -r