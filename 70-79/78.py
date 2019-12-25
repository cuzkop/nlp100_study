# 78. 5分割交差検定
# 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

import joblib
import numpy as np
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

def getLabel(val):
    return '+1' if val > 0.5 else '-1'

cv = joblib.load('tmp/cv74-retry.learn')
lr = joblib.load('tmp/lr74-retry.learn')

with open("tmp/features_retry3.txt") as features:
    x = []
    y = []
    for f in features:
        x.append(f[3:].strip())
        y.append(1.0 if f[0] == "+" else 0.0)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
x_train_cv = cv.fit_transform(x_train)
lr.fit(x_train_cv, y_train)

y_test_pred = lr.predict(cv.transform(x_test))

print('正解率 accuracy:', accuracy_score(y_test, y_test_pred))
print('適合率 precision:', precision_score(y_test, y_test_pred))
print('再現率 recall:', recall_score(y_test, y_test_pred))
print('F1スコア f1_score:', f1_score(y_test, y_test_pred))

print(classification_report(y_test, y_test_pred))