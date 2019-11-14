#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb
import sys

import pymongo
from pymongo import MongoClient

cgitb.enable()

client = MongoClient("localhost", 27017)
db = client.artist_db2
collection = db.artist

name = ""
alias = ""
tag = ""
condition = {}
form = cgi.FieldStorage()

# 各検索項目の抽出
if "name" in form:
    name = form["name"].value

if "alias" in form:
    alias = form["alias"].value

if "tag" in form:
    tag = form["tag"].value


# 検索項目に応じた条件の作成
if name != "":
    condition = {"name": name}

if alias != "":
    if len(condition) < 1:
        condition = {"alias": alias}
    else:
        condition = {"$and": [condition, {"alias": alias}]}

if tag != "":
    if len(condition) < 1:
        condition = {"tag": tag}
    elif "$and" in condition:
        condition["$and"].append({"tag": tag})
    else:
        condition = {"$and": [condition, {"tag": tag}]}

print("Content-Type: text/html")
print()
print('<html><head><title>69</title> \
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> \
        </head><body>')

if len(condition) < 1:
    print("<p>検索結果はありません</p>")
    print("</body></html>")
    sys.exit()

results = collection.find(condition)
results.sort("rating.count", pymongo.DESCENDING)
for result in results:
    # print(result)
    print("<p><b>ID</b>：{}</p>".format(result["id"]))
    print("<p><b>名前</b>：{}</p>".format(result["name"]))
    if "aliases" in result:
        aliases = result["aliases"][0]["name"]
    else:
        aliases = "なし"
    print("<p><b>別名</b>：{}</p>".format(aliases))
    if "area" in result:
        area = result["area"]
    else:
        area = "なし"
    print("<p><b>活動場所</b>：{}</p>".format(area))
    if "tags" in result:
        tag = "/".join(tag["value"] for tag in result["tags"])
    else:
        tag = "なし"
    print("<p><b>タグ</b>：{}</p>".format(tag))
    print("<br>")

print("</body></html>")
sys.exit()
