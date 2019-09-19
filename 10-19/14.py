# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys

argv = sys.argv
n = int(argv[1])

with open("tmp/hightemp.txt") as f:
    for i, l in enumerate(f):
        print(l, end="")
        if i == n-1:
            break

# head -n 5 hightemp.txt