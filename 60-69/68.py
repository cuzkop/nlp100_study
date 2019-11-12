# 68. ソート
# "dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．

import pymongo
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.artist_db2
collection = db.artist

dances = collection.find({"tags.value": "dance"})
dances.sort("rating.count", pymongo.DESCENDING)

for dance in dances.limit(10):
    print(dance["name"])
