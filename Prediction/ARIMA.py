# evaluate an ARIMA model using a walk-forward validation
import pandas as pd
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt


dataset = pd.read_csv('../Datasets/input.csv')
y = dataset['D_Total']
# split into train and test sets
X = dataset['D_Total']
train = X[:280]
test = X[280:]
test = test.reset_index()
test = test.drop(columns=['index'])
print(test)
history = [x for x in train]
print(history)
predictions = list()



for t in range(len(test)):
	model = ARIMA(history, order=(2, 0,0))
	model_fit = model.fit()
	output = model_fit.forecast()
	print(output)
	yhat = output[0]
	predictions.append(yhat)
	obs = test.iloc[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
# evaluate forecasts
# rmse = sqrt(mean_squared_error(test, predictions))
# print('Test RMSE: %.3f' % rmse)
# plot forecasts against actual outcomes
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()



