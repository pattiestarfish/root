#K-Means step 1: initializing K random clusters for initial clusters
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
samples = iris.data

#[:,0] = [all_rows, column_0]
x = samples[:,0]
y = samples[:,1]

# Number of clusters
k=3
# Create x coordinates of k random centroids
centroids_x = np.random.uniform(min(x),max(x),k)
# Create y coordinates of k random centroids
centroids_y = np.random.uniform(min(y),max(y),k)
# Create centroids array, contains all initial centroids
centroids = np.array(list(zip(centroids_x,centroids_y)))
# Make a scatter plot of x, y; alpha darkens features with multiple identical points
plt.scatter(x,y,alpha=0.5)
# Make a scatter plot of the centroids
plt.scatter(centroids_x,centroids_y)
# Display plot
plt.show()

#step 2
import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

iris = datasets.load_iris()

samples = iris.data

x = samples[:,0]
y = samples[:,1]

sepal_length_width = np.array(list(zip(x, y)))

# Step 1: Place K random centroids
k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)

centroids = np.array(list(zip(centroids_x, centroids_y)))

# Step 2: Assign samples to nearest centroid -------------------

# Distance formula
def distance(a,b):
  a_temp = (a[0] - b[0]) ** 2
  b_temp = (a[1] - b[1]) ** 2
  distance = (a_temp + b_temp) ** 0.5
  return distance

# Cluster labels for each point (either 0, 1, or 2)
labels = [0 for x in samples]

#can also use np.zeros(creates empty list of 0 of len parameter)
distances = [0 for x in range(k)]

# Distances to each centroid
for i in range(len(samples)):
  distances[0] = (distance(sepal_length_width[i],centroids[0]))
  distances[1] = (distance(sepal_length_width[i],centroids[1]))
  distances[2] = (distance(sepal_length_width[i],centroids[2]))
  cluster = np.argmin(distances)
  labels[i] = cluster
  i += 1

# Print labels
print(labels)

# Step 3: Update centroids using avg of assigned points by row
#save old centroids first
centroids_old = deepcopy(centroids)
j=0
for i in range(k):
  points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j]==i]
  centroids[i] = np.mean(points, axis=0)
print(centroids_old)
print(centroids)

#for step 4, place steps 2 and 3 in while loop to execute until centroids converge (approach 0)
# Initialize error:
error = np.zeros(3)

error[0] = distance(centroids[0], centroids_old[0])
error[1] = distance(centroids[1], centroids_old[1])
error[2] = distance(centroids[2], centroids_old[2])

# Repeat Steps 2 and 3 until convergence:

while error.all() != 0:

  # Step 2: Assign samples to nearest centroid

  for i in range(len(samples)):
    distances[0] = distance(sepal_length_width[i], centroids[0])
    distances[1] = distance(sepal_length_width[i], centroids[1])
    distances[2] = distance(sepal_length_width[i], centroids[2])
    cluster = np.argmin(distances)
    labels[i] = cluster

  # Step 3: Update centroids

  centroids_old = deepcopy(centroids)

  for i in range(3):
    points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
    centroids[i] = np.mean(points, axis=0)

  error[0] = distance(centroids[0], centroids_old[0])
  error[1] = distance(centroids[1], centroids_old[1])
  error[2] = distance(centroids[2], centroids_old[2])

colors = ['r', 'g', 'b']

for i in range(k):
  points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
  plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)

plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

plt.show()