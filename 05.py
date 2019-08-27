# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

str = "I am an NLPer"
for i in range(len(str) - 2 + 1):
    print(str[i:i+2])

for i in range(len(str.split(" ")) - 2 + 1):
    print(str.split(" ")[i:i+2])