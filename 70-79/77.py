# 77. 正解率の計測
# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

import joblib
import numpy as np
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score

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

print('正解率 accuracy:', accuracy_score(y_test, y_test_pred))
print('適合率 precision:', precision_score(y_test, y_test_pred))
print('再現率 recall:', recall_score(y_test, y_test_pred))
print('F1スコア f1_score:', f1_score(y_test, y_test_pred))

print(classification_report(y_test, y_test_pred))