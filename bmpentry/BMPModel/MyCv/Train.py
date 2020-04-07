
import pandas as pd
from sklearn.externals import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm

df = pd.read_csv('first_csv/S1ResultAll.csv')
# df = pd.read_csv('second_csv/S3ResultALL.csv')

col = ["RatioR", "RatioG", "RatioBg"]
X_all = df[col]
Y_all = df["Result"]
X_np_all = X_all
Y_np_all = Y_all

# 训练集，测试集切分
X_np_train, X_np_test, Y_np_train, Y_np_test = train_test_split(X_np_all, Y_np_all, random_state=1, train_size=0.9)


# 使用svm
# clf = svm.SVC(C=10, kernel='rbf', gamma=4, decision_function_shape='ovr')
clf = svm.SVC(C=1, kernel='linear', gamma=0.01, decision_function_shape='ovo')
clf.fit(X_np_train, Y_np_train)

grade = clf.score(X_np_train, Y_np_train)
y_hat = clf.predict(X_np_train)
print("训练集精度 : " + str(grade))
# print("y_hat_1 : " + str(y_hat))

grade = clf.score(X_np_test, Y_np_test)
y_hat = clf.predict(X_np_test)
# show_accuracy(y_hat, X_np_test, '测试集')
print("测试集精度 : " + str(grade))

from sklearn.linear_model import LogisticRegression

# 逻辑回归
lr_model = LogisticRegression()  # 调用模型，但是并未经过任何调参操作，使用默认值
lr_model.fit(X_np_train, Y_np_train)  # 训练模型
grade = lr_model.score(X_np_train, Y_np_train)
y_hat = lr_model.predict(X_np_train)
print(y_hat)
print("训练集精度 : " + str(grade))
print("逻辑回归")
print(lr_model.score(X_np_test, Y_np_test))  # 获取测试集的评分

joblib.dump(lr_model, '''mmodel/train_all.m''')


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X_np_train)
y_kmeans = kmeans.predict(X_np_test)
print("聚类")
print(kmeans.score(X_np_test, Y_np_test))





from sklearn import svm
from sklearn.model_selection import GridSearchCV

# svm范围内部自动探测
svr = svm.SVC()
parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 2, 3, 4,5,6,7,8,8,10], 'gamma': [0.01, 0.1,0.125, 0.25, 0.5, 1, 2, 4]}
clf = GridSearchCV(svr, parameters, scoring='f1')
clf.fit(X_np_train, Y_np_train)
print('The parameters of the best model are: ')
print(clf.best_params_)

# {'C': 4, 'gamma': 4, 'kernel': 'rbf'}
# 训练集精度 : 0.5617283950617284
# 测试集精度 : 0.5


X_np_train, X_np_test, Y_np_train, Y_np_test = train_test_split(X_np_train, Y_np_train, random_state=1, train_size=0.9)
lr_model = LogisticRegression()  # 调用模型，但是并未经过任何调参操作，使用默认值
lr_model.fit(X_np_train, Y_np_train)  # 训练模型
grade = lr_model.score(X_np_train, Y_np_train)
y_hat = lr_model.predict(X_np_train)
# print(y_hat)
print("训练集精度 : " + str(grade))
print("逻辑回归")
print(lr_model.score(X_np_test, Y_np_test))  # 获取测试集的评分


### h3查看决策函数
# print('decision_function:\n', clf.decision_function(X_np_train))
# print('\npredict:\n', clf.predict(X_np_train))
# 核的类别
# kernel ：核函数，默认是rbf，可以是
# + linear
# 线性：u’v
# + poly
# 多项式：(gamma * u’ * v + coef0) ^ degree
# + rbf
# RBF函数：exp(-gamma | u - v | ^ 2)
# + sigmoid
# sigmoid：tanh(gamma * u’*v + coef0)
# + precomputed

# # 高斯核
# clf_2 = svm.SVC(C=1,
#             kernel='rbf',
#             degree=3,
#             gamma='auto',
#             coef0=0.0,
#             shrinking=True,
#             probability=False,
#             tol=0.001,
#             cache_size=200,
#             class_weight=None,
#             verbose=False,
#             max_iter=-1,
#             decision_function_shape='ovo',
#             random_state=None)
# clf_2.fit(X_np_train, Y_np_train.values.ravel())
#
# grade = clf_2.score(X_np_train, Y_np_train)
# y_hat = clf_2.predict(X_np_train)
# print("训练集精度 : " + str(grade))
# # print("y_hat_1 : " + str(y_hat))
#
# grade = clf_2.score(X_np_test, Y_np_test)
# y_hat = clf_2.predict(X_np_test)
#
# print("测试集精度 : " + str(grade))
# # print("y_hat_1 : " + str(y_hat))


# clf_3 = svm.SVC(C=0.5, kernel='poly', degree=1, gamma=90, decision_function_shape='ovo')
# clf_3.fit(X_np_train, Y_np_train.values.ravel())
#
# grade = clf_3.score(X_np_train, Y_np_train)
# y_hat = clf_3.predict(X_np_train)
#
# print("训练集精度 : " + str(grade))
# print("y_hat_1 : " + str(y_hat))
#
#
# grade = clf_3.score(X_np_test, Y_np_test)
# y_hat = clf_3.predict(X_np_test)
#
# print("测试集精度 : " + str(grade))
# print("y_hat_1 : " + str(y_hat))
#
#
#
#
# import matplotlib.pyplot as plt
#
#
# def getRBFGrade(c: list, gamma: int, X_np_train, Y_np_train, X_np_test, Y_np_test):
#     grades = []
#     for one in c:
#         clf_tmp = svm.SVC(C=one, kernel='rbf', gamma=gamma, decision_function_shape='ovo')
#         clf_tmp.fit(X_np_train, Y_np_train.values.ravel())
#         grade = clf_tmp.score(X_np_test, Y_np_test)
#         grades.append(grade)
#     return grades
#
#
# def getPOLYGrade(c: float, degree: int, gamma: int, X_np_train, Y_np_train, X_np_test, Y_np_test):
#     grades = []
#     for one in c:
#         clf_tmp = svm.SVC(C=one, kernel='poly', degree=degree, gamma=gamma, decision_function_shape='ovo')
#         clf_tmp.fit(X_np_train, Y_np_train.values.ravel())
#         grade = clf_tmp.score(X_np_test, Y_np_test)
#         grades.append(grade)
#     return grades
#
#
# def getRBFGrade2(c: float, gamma: list, X_np_train, Y_np_train, X_np_test, Y_np_test):
#     grades = []
#     for one in gamma:
#         clf_tmp = svm.SVC(C=c, kernel='rbf', gamma=one, decision_function_shape='ovo')
#         clf_tmp.fit(X_np_train, Y_np_train.values.ravel())
#         grade = clf_tmp.score(X_np_test, Y_np_test)
#         grades.append(grade)
#     return grades
#
#
# def getPOLYGrade2(c: float, degree: int, gamma: int, X_np_train, Y_np_train, X_np_test, Y_np_test):
#     grades = []
#     for one in gamma:
#         clf_tmp = svm.SVC(C=c, kernel='poly', degree=degree, gamma=one, decision_function_shape='ovo')
#         clf_tmp.fit(X_np_train, Y_np_train.values.ravel())
#         grade = clf_tmp.score(X_np_test, Y_np_test)
#         grades.append(grade)
#     return grades
#
#
# #### 测试精度随着c变化趋势【高斯核】
# list_c = np.arange(0.1, 1, 0.1)
# grade = getRBFGrade(list_c, 120, X_np_train, Y_np_train, X_np_test, Y_np_test)
# plt.scatter(list_c, grade, color="red")
# plt.show()
#
#
# #### 测试精度随着gamma的变化【高斯核】
# list_c = np.arange(10, 200, 10)
# grade = getRBFGrade2(0.8, list_c, X_np_train, Y_np_train, X_np_test, Y_np_test)
# plt.scatter(list_c, grade, color="blue")
# plt.show()
#
#
# list_c = np.arange(10, 200, 10)
# grade = getRBFGrade2(0.5, list_c, X_np_train, Y_np_train, X_np_test, Y_np_test)
# plt.scatter(list_c, grade, color="blue")
# plt.show()
#
#
# #### 测试精度随着c的变化【多项式核】
#
# list_c = np.arange(0.1, 1, 0.1)
# grade = getPOLYGrade(list_c, 1, 120, X_np_train, Y_np_train, X_np_test, Y_np_test)
# plt.scatter(list_c, grade, color="red")
# plt.show()
#
#
# #### 测试精度随着gamma的变化【多项式核】
#
# list_c = np.arange(10, 200, 10)
# grade = getPOLYGrade2(0.3, 1, list_c, X_np_train, Y_np_train, X_np_test, Y_np_test)
# plt.scatter(list_c, grade, color="blue")
# plt.show()
#
#

