# 79. 適合率-再現率グラフの描画
# ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

from sklearn.metrics import precision_recall_curve
import joblib
import numpy as np
from sklearn.metrics import classification_report, accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import sys

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

pred_positive = lr.predict_proba(cv.transform(x_test))[:, 1]
precisions, recalls, thresholds = precision_recall_curve(y_test, pred_positive)

for i in range(21):
    close_point = np.argmin(np.abs(thresholds - (i * 0.05)))
    plt.plot(precisions[close_point], recalls[close_point], 'o')

plt.plot(precisions, recalls)
plt.xlabel('Precision')
plt.ylabel('Recall')

plt.show()
input()