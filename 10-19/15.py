# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

import sys

argv = sys.argv
n = int(argv[1])

with open("tmp/hightemp.txt") as f:
    for l in range(n):
        print(next(f), end="")

# tail -n 2 hightemp.txt