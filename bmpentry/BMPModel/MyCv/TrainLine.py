from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import time
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import pandas as pd


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)

    linear_regression = LinearRegression(normalize=True)
    pipeline = Pipeline([('polynomial_features', polynomial_features),
                         ('linear_regression', linear_regression)])
    return pipeline


data = pd.read_csv('first_csv/resultAll.csv')
col = ["RatioR", "RatioG"]
X_all = data[col]
Y_all = data["Result"]

X_train, X_test, y_train, y_test = train_test_split(X_all, Y_all, test_size=0.2, random_state=3)

for i in range(1, 4):
    print('degree:{}'.format(i))
    model = polynomial_model(degree=i)

    start = time.clock()
    model.fit(X_train, y_train)

    train_score = model.score(X_train, y_train)
    cv_score = model.score(X_test, y_test)

    print('time used:{0:.6f}; train_score:{1:.6f}, sv_score:{2:.6f}'.format((time.clock() - start),
                                                                            train_score, cv_score))
