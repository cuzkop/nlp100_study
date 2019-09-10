# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

cnt = 0
with open("hightemp.txt", "r") as f:
    for l in f:
        cnt += 1

print(cnt)