from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
from copy import deepcopy

#step 1: creating and visualizing data
#possible truth table values for OR gate
#AND gate does not get properly fitted
data = [[0,0],[0,1],[1,0],[1,1]]
labels = [0,1,1,1]
class_weight = {0:1, 1:10}

x = [point[0] for point in data]
y = [point[1] for point in data]

plt.scatter(x,y,c=labels)
plt.show()
#Step 2: Building Perceptron
classifier = Perceptron(max_iter=1000,class_weight=None)
#classifier = deepcopy(classifier)

#training AND data
classifier.fit(data, labels,sample_weight=None)
print(classifier.predict([[0.5, 0.5]]))
print(classifier.predict([[1, 1]]))
print(classifier.predict([[0.55, 0.55]]))

#Step 3: Visualizing Perceptron
#create a heat map to visualize decision boundary using a range of evenly spaced x and y values
x_values = np.linspace(0,1,100)
y_values = np.linspace(0,1,100)
point_grid = list(product(x_values,y_values))
distances = classifier.decision_function(point_grid)
#i=0
#for distance in distances:
#    print(str(i) + "iter" + str(distance))
#    i += 1
abs_distances = [abs(distance) for distance in distances]

#converting 10,000 num list into 100x100 2D array
distances_matrix = np.reshape(abs_distances, (100,100))

#pcolormesh parameters: 2D list
heatmap = plt.pcolormesh(x_values,y_values,distances_matrix)
plt.colorbar(heatmap)

print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))
print(classifier.score(data, labels))

plt.show()

#training OR data
#oor_data = [[0,0],[1,0],[0,1],[1,1]]
#or_labels = [0,1,1,1]
#orx = [point[0] for point in or_data]
#ory = [point[1] for point in or_data]
#or_model = classifier.fit(or_data,or_labels)
#print(or_model.score(or_data,or_labels))

#training XOR data
#xor_data = [[0,0],[1,0],[0,1],[1,1]]
#xor_labels = [0,1,1,0]
#xorx = [point[0] for point in xor_data]
#xory = [point[1] for point in xor_data]
#xor_model = classifier.fit(xor_data,xor_labels)
#print(xor_model.score(xor_data,xor_labels))