# 67. 複数のドキュメントの取得
# 特定の（指定した）別名を持つアーティストを検索せよ．

import sys
from pymongo import MongoClient

argv = sys.argv
artist_name = str(argv[1])

client = MongoClient("localhost", 27017)
db = client.artist_db2
collection = db.artist

for artist in collection.find({'name':artist_name}):
    if "aliases" in artist:
        print(artist["aliases"][0]["name"])