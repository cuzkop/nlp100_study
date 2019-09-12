# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open("hightemp.txt", "r") as f:
    for l in f:
        print(l.replace("\t", " "), end="")
