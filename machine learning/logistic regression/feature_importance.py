#determines how much weight each feature carries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from exam import exam_features_scaled, passed_exam_2

# Train a sklearn logistic regression model on the normalized exam data
model_2 = LogisticRegression()
model_2.fit(exam_features_scaled,passed_exam_2)

# Assign and update coefficients
coefficients = model_2.coef_
#
coefficients = coefficients.tolist()[0]

# Plot bar graph
plt.bar([1,2],coefficients)
plt.xticks([1,2],['hours studied','math courses taken'])
plt.xlabel('feature')
plt.ylabel('coefficient')
plt.show()
#---------------------------------------------
#Classification Thresholding
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


