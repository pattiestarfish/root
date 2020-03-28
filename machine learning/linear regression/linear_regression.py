import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 8
#intercept:
b = 40


y = [month*m + b for month in months]
plt.plot(months, y)
plt.plot(months, revenue, "o")
#plot your line here:

plt.show()
#------------------
regression+gradients
def get_gradient_at_b(x,y,m,b):
  diff = 0
  for i in range(len(x)):
    diff += (y[i]-(m*x[i]+b))
  b_gradient = -2/len(x) * diff
  return b_gradient

def get_gradient_at_m(x,y,m,b):
  diff = 0
  for i in range(len(x)):
    diff += x[i]*(y[i] - (m * x[i] + b))
    m_gradient = -2/len(x) * diff
  return m_gradient
#--------------------------
def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff
  return m_gradient

# Define your step_gradient function here
def step_gradient(x,y,b_current,m_current):
  b_gradient = get_gradient_at_b(x, y, b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01  * b_gradient)
  m = m_current - (0.01 * m_gradient)
  return [b, m]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# current intercept guess:
b = 0
# current slope guess:
m = 0

# Call your function here to update b and m
b,m = step_gradient(months, revenue, b, m                                                                               )
print(b, m)
#------------------
#linear regression on real data

import codecademylib3_seaborn
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]
b,m = gradient_descent(X,y,0.0001,1000)
plt.plot(X, y, 'o')
#plot your line here:
y_predictions = [height*m + b for height in X]
plt.plot(X, y_predictions)
plt.show()