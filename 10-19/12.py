# 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

with open("hightemp.txt", "r") as f, open("col1.txt", "w") as col1, open("col2.txt", "w") as col2:
    for l in f:
        cols = l.split("\t")
        col1.write(cols[0]+"\n")
        col2.write(cols[1]+"\n")
        

# 確認方法
# $ cut -f 1 hightemp.txt > col1_conf.txt
# $ cut -f 2 hightemp.txt > col2_conf.txt
# $ diff col1.txt col1_conf.txt
# $ diff col2.txt col2_conf.txt