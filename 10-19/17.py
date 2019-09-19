# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

with open("tmp/hightemp.txt", "r") as f:
    files = f.readlines()


s = set()
for l in files:
    lst = l.split("\t")
    s.add(lst[0])

print(s)

# cut -f 1 tmp/hightemp.txt | sort | uniq