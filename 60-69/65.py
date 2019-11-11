# 65. MongoDBの検索
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．さらに，これと同様の処理を行うプログラムを実装せよ．

import json
from pymongo import MongoClient 

client = MongoClient("localhost", 27017)
db = client.artist_db2
collection = db.artist

for queen in collection.find({'name':'Queen'}):
    for q in queen.values():
        print(q)