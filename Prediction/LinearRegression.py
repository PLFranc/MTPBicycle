import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
def pred(data):
    df = pd.read_csv('../Datasets/Dataset_clean.csv')
    df['hollyday'] = df['hollyday'].replace(0.4, 0)
    columns = [column for column in df if column not in
               ['Date', 'Y_Total', 'D_Total']]
    X = df[columns]
    y = df['D_Total']

    pipeline = Pipeline([('poly_features', PolynomialFeatures(degree=2)),
                         ('ols', LinearRegression())])
    pipeline.fit(X, y)

    # print(100 * r2_score(y, pipeline.predict(X)))
    #
    # print(np.sqrt(mean_squared_error(y, pipeline.predict(X))))
    #
    # print(pipeline[0].get_feature_names())  # features name
    # print(pipeline[1].coef_)  # coefficients
    return pipeline.predict(data)
