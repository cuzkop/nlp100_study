# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys
import math

argv = sys.argv
n = int(argv[1])

with open("hightemp.txt", "r") as f:
    files = f.readlines()

cnt = len(files)
spl =  math.ceil(cnt/n)

for loop in range(0, cnt, spl):
    with open("split_{}.txt".format(loop), "w") as s:
        for l in files[loop:loop+spl]:
            s.write(l)
        

# split -l ${spl} hightemp.txt