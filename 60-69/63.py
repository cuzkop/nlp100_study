# 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

import redis
import json
import sys

argv = sys.argv
artist_name = str(argv[1])

redis = redis.Redis(host="localhost", port=6379, db=0)

with open("tmp/artist.json", "r") as file:
    cnt = 0
    for f in file:
        line = json.loads(f)
        # print(type(str(line.get("tags", ""))))
        redis.set(line["name"], str(line.get("tags", "")))
        if cnt == 30:
            break
        cnt+=1

string_tags = redis.get(artist_name)
tags = json.loads(str(string_tags, encoding="utf-8").replace("'", '"'))
print(type(tags))


# if "tags" in line:
#             for tag in line["tags"]:
#                 print(tag["count"])
#         cnt += 1
#         if cnt == 30:
#             sys.exit()