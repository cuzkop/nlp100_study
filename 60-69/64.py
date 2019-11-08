# 64. MongoDBの構築
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value

import json
import pymongo
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
db = client.artist_db
collection = db.artist

with open("tmp/artist.json", "r") as file:
    cnt = 0
    insert = []
    for f in file:
        line = json.loads(f)
        insert.append(line)

    collection.insert_many(insert)

collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])