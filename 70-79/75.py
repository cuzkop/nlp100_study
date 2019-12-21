# 75. 素性の重み
# 73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．

import joblib
import numpy as np

cv = joblib.load('tmp/cv74-retry.learn')
lr = joblib.load('tmp/lr74-retry.learn')

sorted_coef_idx = np.argsort(lr.coef_)[0]
feature_names = cv.get_feature_names()


print('重みの高い素性トップ10')
for i in sorted_coef_idx[-1:-11:-1]:
    print(feature_names[i])

print()
print('重みの低い素性トップ10')
for i in sorted_coef_idx[:10]:
    print(feature_names[i])
