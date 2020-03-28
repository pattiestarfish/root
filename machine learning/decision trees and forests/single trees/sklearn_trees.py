import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

#loads csv data into flags, with row 0 as header
flags = pd.read_csv('flags.csv', header = 0)
print(flags.columns)
print(flags.head())

#obtains specific columns from dataframe
labels = flags[['Landmass']]
data = flags[["Red", "Green", "Blue", "Gold",
 "White", "Black", "Orange",
 "Circles",
"Crosses","Saltires","Quarters","Sunstars",
"Crescent","Triangle"]]

#tree instantiation w/ pruning to increase accuracy
scores=[]
for i in range(1,21):
  train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2,random_state=1)

#initializing tree with constructor
  tree = DecisionTreeClassifier(random_state=1, max_depth = i)

#creating tree to fit to training data
  model = tree.fit(train_data, train_labels)

#prints each model's accuracy (i on [1,20])
#print(model.score(test_data, test_labels))
  scores.append(model.score(test_data, test_labels))

plt.plot(range(1,21), scores)
plt.show()

