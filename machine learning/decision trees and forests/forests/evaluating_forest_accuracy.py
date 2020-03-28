from tree import training_data, training_labels, testing_data, testing_labels, make_random_forest, make_single_tree, \
    classify
import numpy as np
import random

np.random.seed(1)
random.seed(1)

# tree made without bagging, 1 row per new tree
tree = make_single_tree(training_data, training_labels)
forest = make_random_forest(40, training_data, training_labels)

# initialize variables to count num correct
single_tree_correct = 0
forest_correct = 0

# loops through every point in test set, compares to actual tree value
# and returns percentage of correctly classified points
for i in range(len(testing_data)):
    prediction = classify(testing_data[i], tree)
    if prediction == testing_labels[i]:
        single_tree_correct += 1
    predictions = []
    for forest_tree in forest:
        predictions.append(classify(testing_data[i], forest_tree))
    forest_prediction = max(predictions, key=predictions.count)
    if forest_prediction == testing_labels[i]:
        forest_correct += 1

# prints accuracy for single decision tree
print("Single tree accuracy: " + str(single_tree_correct / len(testing_data)))
print("Forest of trees accuracy: " + str(forest_correct / len(testing_data)))
