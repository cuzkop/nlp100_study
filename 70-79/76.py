# 76. ラベル付け
# 学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

import joblib
import numpy as np

def getLabel(val):
    return '+1' if val > 0.5 else '-1'

cv = joblib.load('tmp/cv74-retry.learn')
lr = joblib.load('tmp/lr74-retry.learn')

with open("tmp/features_retry3.txt") as features:
    x_test = []
    y_test = []
    for f in features:
        x_test.append(f[3:].strip())
        y_test.append(1.0 if f[0] == "+" else 0.0)

y_test_pred = lr.predict(cv.transform(x_test))
pr = lr.predict_proba(cv.transform(x_test))

cnt = 0
for right, pred, proba in zip(y_test, y_test_pred, pr):
    print('{}\t{}\t{}'.format(getLabel(right), getLabel(pred), proba[0] if pred == 0 else proba[1]))
    cnt += 1
    if cnt == 20:
        break

