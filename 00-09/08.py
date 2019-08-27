# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．英小文字ならば(219 - 文字コード)の文字に置換その他の文字はそのまま出力この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(string):
    rt = ""
    for s in string:
        if "a" <= s <= "z":
            rt += chr(219 - ord(s))
        else:
            rt += s
    return rt

cipher("ABCdef")
print(cipher("AaAaAaAa"))