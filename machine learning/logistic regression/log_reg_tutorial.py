import numpy as np
from exam import hours_studied, calculated_coefficients, intercept

# Create your log_odds() function here
def log_odds(features, coefficients, intercept):
  prod = np.dot(features,coefficients) + intercept
  return prod

# Calculate the log-odds for the Codecademy University data here
calculated_log_odds = log_odds(hours_studied, calculated_coefficients, intercept)
print(calculated_log_odds)

def sigmoid(z):
  denominator = 1 + np.exp(-z)
  return 1/denominator

# Calculate the sigmoid of the log-odds here
probabilities = sigmoid(calculated_log_odds)
print(probabilities)
#------------------------------------------------------
import numpy as np
from exam import hours_studied, calculated_coefficients, intercept


def log_odds(features, coefficients, intercept):
  return np.dot(features, coefficients) + intercept


def sigmoid(z):
  denominator = 1 + np.exp(-z)
  return 1 / denominator


# Create predict_class() function here
def predict_class(features, coefficients, intercept, threshold):
  calculated_log_odds = log_odds(features, coefficients, intercept)
  probabilities = sigmoid(calculated_log_odds)
  return np.where(probabilities >= threshold, 1, 0)


# Make final classifications on Codecademy University data here
final_results = predict_class(hours_studied, calculated_coefficients, intercept, 0.5)
print(final_results)