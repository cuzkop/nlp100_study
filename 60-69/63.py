# 63. オブジェクトを値に格納したKVS
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．

import redis
import json
import sys

argv = sys.argv
artist_name = str(argv[1])

redis = redis.Redis(host="localhost", port=6379, db=0)

# ここは重すぎるので最初のみ
# with open("tmp/artist.json", "r") as file:
#     for f in file:
#         line = json.loads(f)
#         redis.set(line["name"], str(line.get("tags", "")))

string_tags = redis.get(artist_name)
if str(string_tags, encoding="utf-8") == "":
    print("None")
    sys.exit()

tags = json.loads(str(string_tags, encoding="utf-8").replace("'", '"'))

for tag in tags:
    print("value : {}, count : {}".format(tag["value"], tag["count"]))