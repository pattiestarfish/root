import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
samples = iris.data
model = KMeans(n_clusters=3)
model.fit(samples)

# Store the new Iris measurements
new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
   [6.5, 3. , 5.5, 0.4],
   [5.8, 2.7, 5.1, 1.9]])
# Predict labels for the new_samples
labels = model.predict(new_samples)
print(labels)
#------------------------
#visualizing data after KMeans
import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
samples = iris.data
model = KMeans(n_clusters=3)
model.fit(samples)
labels = model.predict(samples)
print(labels)

# Make a scatter plot of x and y and using labels to define the colors
x = samples[:,0]
y = samples[:,1]
plt.scatter(x,y,c=labels,alpha=0.5)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()
#evaluating data with cross tabulation------------------------
species = np.chararray(target.shape, itemsize=150)

for i in range(len(samples)):
    if target[i] == 0:
        species[i] = 'setosa'
    elif target[i] == 1:
        species[i] = 'versicolor'
    elif target[i] == 2:
        species[i] = 'virginica'

df = pd.DataFrame({'labels': labels, 'species': species})
print(df)

ct = pd.crosstab(df['labels'], df['species'])
print(ct)

#determining number of clusters
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
samples = iris.data

# Code Start here:
num_clusters = [x for x in range(1,9)]
inertias = []
for num in num_clusters:
  model = KMeans(num)
  model.fit(samples)
  inertias.append(model.inertia_)
plt.plot(num_clusters, inertias, '-o')
#graph shows num clusters vs inertia(lower better)
plt.show()