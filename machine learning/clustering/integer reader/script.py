import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
# prints entire dataset
print(digits)
# prints description of dataset
print(digits.DESCR)
# prints list containing 64 values of pixel image color(0-16)
print(digits.data)
# prints result of dataset, first num is 0, last is 8
print(digits.target)

plt.gray()

plt.matshow(digits.images[100])

plt.show()

# prints target label at index 100
print(digits.target[100])

# creating and training model using sklearn
model = KMeans(n_clusters=10, init='k-means++', random_state=42)
model.fit(digits.data)

# creates figure
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')

for i in range(10):
    # Initialize subplots in a grid of 2X5, at i+1th position
    ax = fig.add_subplot(2, 5, 1 + i)

    # Display images
    ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
    [0.00, 3.19, 6.01, 6.09, 6.09, 5.56, 0.38, 0.00, 1.83, 6.92, 2.81, 1.52, 1.52, 5.71, 6.01, 2.13, 0.00, 0.00, 0.00,
     0.00, 0.00, 0.22, 4.49, 7.62, 0.00, 0.00, 0.08, 1.83, 3.73, 5.71, 7.47, 4.56, 0.00, 0.00, 1.14, 7.53, 7.61, 7.61,
     6.17, 2.13, 0.00, 0.00, 0.00, 0.00, 1.29, 1.68, 4.65, 4.88, 0.00, 0.00, 0.00, 0.00, 0.00, 0.23, 3.58, 5.34, 0.91,
     4.88, 5.34, 5.95, 6.09, 7.16, 6.85, 2.89],
    [0.00, 0.00, 3.04, 7.47, 7.39, 5.48, 1.07, 0.00, 0.00, 0.46, 6.86, 2.74, 1.06, 4.87, 6.24, 0.00, 0.00, 3.58, 5.79,
     0.08, 0.00, 0.38, 7.61, 0.00, 0.00, 3.81, 3.81, 0.00, 0.00, 0.45, 7.61, 0.00, 0.00, 3.81, 4.80, 0.00, 0.00, 1.98,
     6.47, 0.00, 0.00, 1.82, 6.86, 0.00, 0.00, 3.50, 5.09, 0.00, 0.00, 0.23, 7.16, 2.21, 0.53, 7.00, 2.58, 0.00, 0.00,
     0.00, 3.72, 7.31, 6.32, 6.01, 0.00, 0.00],
    [0.00, 0.76, 5.56, 7.39, 7.09, 5.40, 0.46, 0.00, 0.00, 4.42, 5.33, 0.68, 0.76, 6.01, 4.26, 0.00, 0.00, 4.42, 3.89,
     0.00, 0.00, 2.44, 5.63, 0.00, 0.00, 3.20, 4.57, 0.00, 0.00, 1.60, 6.09, 0.00, 0.00, 2.74, 5.49, 0.00, 0.00, 1.83,
     6.09, 0.00, 0.00, 1.67, 7.16, 0.23, 0.00, 2.44, 5.40, 0.00, 0.00, 0.00, 6.32, 3.81, 0.08, 5.02, 4.48, 0.00, 0.00,
     0.00, 1.90, 7.30, 7.15, 6.92, 1.29, 0.00],
    [0.00, 0.00, 0.08, 4.26, 7.39, 2.44, 0.00, 0.00, 0.00, 0.08, 4.49, 6.63, 1.29, 0.00, 0.00, 0.00, 0.00, 2.97, 6.86,
     1.14, 0.53, 0.69, 0.00, 0.00, 0.08, 6.32, 3.80, 5.26, 7.46, 7.39, 6.17, 0.84, 1.90, 7.16, 6.09, 6.01, 0.91, 0.23,
     5.09, 5.25, 1.90, 7.62, 5.78, 0.30, 0.00, 0.00, 3.05, 5.09, 0.00, 5.86, 5.10, 1.52, 0.30, 0.84, 6.09, 3.65, 0.00,
     0.99, 5.24, 6.77, 7.61, 7.61, 5.25, 0.38]
])

new_labels = model.predict(new_samples)

for i in range(len(new_labels)):
    if new_labels[i] == 0:
        print(0, end='')
    elif new_labels[i] == 1:
        print(9, end='')
    elif new_labels[i] == 2:
        print(2, end='')
    elif new_labels[i] == 3:
        print(1, end='')
    elif new_labels[i] == 4:
        print(6, end='')
    elif new_labels[i] == 5:
        print(8, end='')
    elif new_labels[i] == 6:
        print(4, end='')
    elif new_labels[i] == 7:
        print(5, end='')
    elif new_labels[i] == 8:
        print(7, end='')
    elif new_labels[i] == 9:
        print(3, end='')