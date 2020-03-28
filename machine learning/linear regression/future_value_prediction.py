import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df.head())
prod_per_year = (df.groupby('year').totalprod.mean().reset_index())
print(prod_per_year)
X = prod_per_year['year']
X = X.values.reshape(-1,1)
y = prod_per_year['totalprod']
plt.scatter(X,y)
plt.show()
regr = linear_model.LinearRegression()
regr.fit(X,y)
m = regr.coef_[0]
b = regr.intercept_
y_predict = [m*num + b for num in X]
print(y_predict)
y1_predict = regr.predict(X)
print(y1_predict)
plt.plot(X, y_predict)
plt.scatter(X, y1_predict)
plt.show()

#predicting honey decline
X_future = np.array(range(2013,2050))
print(X_future)
X_future = X_future.reshape(-1,1)
#print(X_future)
future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()