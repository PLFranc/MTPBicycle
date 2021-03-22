import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Cropping2D, Lambda, Dropout, MaxPooling2D, Reshape, Input
dataset = pd.read_csv('../Datasets/input.csv')
y = dataset['D_Total']
dataset.drop(columns=['Date'],inplace=True)
dataset.drop(columns=['Y_Total'],inplace=True)
dataset.drop(columns=['D_Total'],inplace=True)
x_train = dataset[:280]
x_test = dataset[280:]

y_train = y[:280]
y_test = y[280:]

batch_size = 15
epochs = 800
model = Sequential()
# x_train.shape[1]

model.add(Dense(10,activation="relu", input_shape=(10,)))
# model.add(Dense(15, activation="relu"))
# model.add(Dense(15, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="relu"))

model.add(Dense(1,activation='linear'))

model.compile(loss='mean_absolute_percentage_error',
              optimizer='Adam',
              metrics=['accuracy'])
model.fit(x_train, y_train,
          validation_data=(x_test, y_test),
          batch_size=batch_size,
          epochs=epochs)
preds = model.predict(x_test)
# compute the difference between the *predicted* house prices and the
# *actual* house prices, then compute the percentage difference and
# the absolute percentage difference
diff = preds.flatten() - y_test
percentDiff = (diff / y_test) * 100
absPercentDiff = np.abs(percentDiff)
# compute the mean and standard deviation of the absolute percentage
# difference
mean = np.mean(absPercentDiff)
std = np.std(absPercentDiff)
print(mean)
print(std)