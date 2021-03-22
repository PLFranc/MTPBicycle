import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from statsmodels.tsa.arima.model import ARIMA


class ConstantP(BaseEstimator, RegressorMixin):

    def __init__(self, p=1, q=1):
        self.p = p
        self.q = q

    def fit(self, X, y=None):
        model = ARIMA(X,order=(self.p,self.q,0))
        model.fit()


    def predict(self, X):
        return self.p * X[:, 1]

dataset = pd.read_csv('../Datasets/input.csv')
y = dataset['D_Total']
x_train = dataset[:280]
x_test = dataset[280:]

y_train = y[:280]
y_test = y[280:]



parameters = {'p': [0, 1, 2, 3, 4], 'q': [1, 2]}
model = ConstantP()
model = GridSearchCV(model, parameters, cv=TimeSeriesSplit())
model.fit(x_train, y_train)
