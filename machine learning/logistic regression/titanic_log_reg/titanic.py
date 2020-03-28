import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
print(type(passengers))
print(passengers.columns)

# Update sex column to numerical
#print(len(passengers['Sex']))
#i=0
#for gender in passengers['Sex']:
#  if gender == 'male':
#      (passengers['Sex'][i]) = 0
#      i += 1
#  else:
#      (passengers['Sex'][i]) = 1
#      i += 1
#1 liner
passengers['Sex'] = passengers['Sex'].map({'male':0,'female':1})
#checking passenger 1 binary Sex
print(passengers['Sex'][0])

# Fill the nan values in the age column
pass_age = (passengers['Age'].values)
mean_age = np.nanmean(pass_age)
print(mean_age)
#mean_age = mean(passengers['Age'].values
passengers['Age'].fillna(value=mean_age,inplace=True)
print(passengers['Age'])

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x==1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x==2 else 0)
print(passengers)

# Select the desired features
features = passengers[['Sex','Age','FirstClass','SecondClass']]
survival = passengers['Survived']
print(features)
print(len(features))
print(len(survival))

# Perform train, test, split
#x_train = training features, y_train training labels; x_test = testing features
train_features, test_features, y_train, y_test = train_test_split(features, survival, test_size=0.2,random_state=1)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)
print(train_features)
print(type(train_features))

#Create and train the model
model = LogisticRegression()
model.fit(train_features, y_train)

# Score the model on the train data
print(model.score(train_features, y_train))

# Score the model on the test data
print(model.score(test_features, y_test))

# Analyze the coefficients
print(model.coef_)

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([0.0,24.0,1.0,0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack,Rose,You])
print(sample_passengers)

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(model.predict(sample_passengers))
print(model.predict_proba(sample_passengers))
