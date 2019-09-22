# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

with gzip.open("tmp/jawiki-country.json.gz", "rt") as f:
    for l in f:
        jl = json.loads(l)
        if jl["title"] == "イギリス":
            print(jl["text"])