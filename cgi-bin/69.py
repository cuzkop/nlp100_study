#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb
import os
import sys

cgitb.enable()

name = ""
alias = ""
tag = ""
condition = {}
form = cgi.FieldStorage()

print ("Content-Type: text/html")
print()

# 各検索項目の抽出
if "name" in form:
    name = form["name"].value

if "alias" in form:
    alias = form["alias"].value

if "tag" in form:
    tag = form["tag"].value


# 検索項目に応じた条件の作成
if name != "":
    condition = {"name" : name}

if alias != "":
    if len(condition) < 1:
        condition = {"alias" : alias}
    else:
        condition = {"$and" : [condition, {"alias" : alias}]}

if tag != "":
    if len(condition) < 1:
        condition = {"tag" : tag}
    elif "$and" in condition:
        condition["$and"].append({"tag" : tag})
    else:
        condition = {"$and" : [condition, {"tag" : tag}]}

print(condition)

sys.exit()

print ("Content-Type: text/html")
print()



print("<html><body>")
print("<h1>TEST</h1>")
print("</body></html>")