import pandas as pd
from sklearn.externals import joblib
import numpy as np
from sklearn import svm

df = pd.read_csv('first_csv/S1ResultAll.csv')

col = ["RatioR", "RatioG", "RatioBg"]

X_all = df[col]
# print(X_all[0:10])
Y_all = df["Result"]

data = {
    'RatioR':[0.061641, 0.15266875, 0.205765625, 0.1449125, 0.138190625, 0.2067375],
    'RatioG':[0, 0.042996875, 0.0, 0.0, 0.0, 0.06869375],
    'RatioOther': [0.938359, 0.804334375, 0.794234375, 0.8550875, 0.861809375, 0.72456875],
}
frame = pd.DataFrame(data)
print(frame)

clf = joblib.load('mmodel/train_all.m')
res = clf.predict(frame)
print(res)