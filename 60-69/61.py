# 61. KVSの検索
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．

import redis
import sys

argv = sys.argv
artist_name = str(argv[1])
redis = redis.Redis(host="localhost", port=6379, db=0)

place = redis.get(artist_name)

if place != None:
    print(str(place, encoding="utf-8"))
else:
    print("None")