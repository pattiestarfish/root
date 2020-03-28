import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# take a list of features to model as a parameter
def model_these_features(feature_list, df, index, i):
    # [] returns row as series whereas [[]] returns as DataFrame(list of labels)
    #returns stars and feature list of respective DataFrames; limits features to predefined subset of data
    outcomes = df.loc[:, index[i]]
    features = df.loc[:, feature_list]

    #returns in order: x training var, x test var, ... takes in input features (independent vars) and ratings (dependent var)
    #splits variables into testing and training pools (typically 80/20 split)
    X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=1)

    #allows function to operate for both single variable and multi variable regressions (reformats array into vertical columns)
    if len(X_train.shape) < 2:
        X_train = np.array(X_train).reshape(-1, 1)
        X_test = np.array(X_test).reshape(-1, 1)

    #instantiates LinearRegression model line, and generates best fit lien onto model
    model = LinearRegression()
    model.fit(X_train, y_train)

    #displays correlation coefficients for training and test scores between -1 and 1; higher carries more weight
    print('Train Score:', model.score(X_train, y_train))
    print('Test Score:', model.score(X_test, y_test))

    # print the model features and their corresponding coefficients, from most predictive to least predictive
    print(sorted(list(zip(feature_list, model.coef_)), key=lambda x: abs(x[1]), reverse=True))

    #determines predicted values from y=mx+b (in this case predicted 'Yelp' ratings)
    y_predicted = model.predict(X_test)

    #plots dependent variables vs predicted values (actual vs predicted)
    plt.scatter(y_test, y_predicted)
    plt.xlabel('Actual ' + index[i])
    plt.ylabel('Predicted ' + index[i])
 #   plt.ylim(1, 5)
    plt.show()