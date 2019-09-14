# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open("col1.txt", "r") as col1, open("col2.txt", "r") as col2, open("merge.txt", "w") as m:
    for c1, c2 in zip(col1, col2):
        c1 = c1.replace("\n", "")
        m.write(c1 + "\t" + c2)
        
# paste col1.txt col2.txt > merge_conf.txt
# diff merge.txt merge_conf.txt