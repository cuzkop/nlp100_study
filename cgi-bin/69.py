#!/usr/bin/env python
# coding: utf-8

import cgi
import cgitb
import os

cgitb.enable()

form = cgi.FieldStorage()

print ("Content-Type: text/html")
print()



print("<html><body>")
print("<h1>TEST</h1>")
print(form["name"].value)
print("</body></html>")