# 62. KVS内の反復処理
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

import redis
import sys

redis = redis.Redis(host="localhost", port=6379, db=0)

cnt = 0
for key in redis.keys():
    if redis.get(str(key, encoding="utf-8")) == "Japan".encode():
        cnt += 1

print(cnt)
