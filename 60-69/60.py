# 第7章: データベース
# artist.json.gzは，オープンな音楽データベースMusicBrainzの中で，アーティストに関するものをJSON形式に変換し，gzip形式で圧縮したファイルである．このファイルには，1アーティストに関する情報が1行にJSON形式で格納されている．JSON形式の概要は以下の通りである．
# artist.json.gzのデータをKey-Value-Store (KVS) およびドキュメント志向型データベースに格納・検索することを考える．KVSとしては，LevelDB，Redis，KyotoCabinet等を用いよ．ドキュメント志向型データベースとして，MongoDBを採用したが，CouchDBやRethinkDB等を用いてもよい．

# 60. KVSの構築
# Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．

import redis
import json
import sys

redis = redis.Redis(host="localhost", port=6379, db=0)

with open("tmp/artist.json", "r") as file:
    cnt = 0
    for f in file:
        line = json.loads(f)
        redis.set(line["name"], line.get("area", ""))
        redis.expire(line["name"], 300)