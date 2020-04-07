# import xlrd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd

# data = xlrd.open_workbook('gua.xlsx')
data = pd.read_csv('first_csv/resultAll.csv')
col = ["RatioR", "RatioG"]
X_all = data[col]
Y_all = data["Result"]
# sheet = data.sheet_by_index(0)
# Density = sheet.col_values(6)
# Sugar = sheet.col_values(7)
# Res = sheet.col_values(8)
# 读取原始数据

# y的尺寸为(17,)
# 从原始数据中选取一半数据进行训练，另一半数据进行测试
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_all, Y_all, test_size=0.5, random_state=0)
# 逻辑回归模型
log_model = LogisticRegression()
# 训练逻辑回归模型
log_model.fit(X_train, y_train)
# 预测y的值
y_pred = log_model.predict(X_test)
# 查看测试结果
print(metrics.confusion_matrix(y_test, y_pred))
print(metrics.classification_report(y_test, y_pred))