# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）

with open("tmp/hightemp.txt", "r") as f:
    files = f.readlines()

nf = sorted(files, key=lambda nf: nf.split("\t")[2])

for l in nf:
    print(l)

# sort tmp/hightemp.txt --key=3