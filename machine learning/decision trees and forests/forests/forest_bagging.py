from tree import car_data, car_labels, split, information_gain, classify
import random
import numpy as np
np.random.seed(1)
random.seed(4)
tree = build_tree(car_data, car_labels)
print(len(car_data))
print(len(car_labels))
#print_tree(tree)

# The features are the price of the car, the cost of maintenance, the number of doors, the number of people the car can hold, the size of the trunk, and the safety rating
unlabeled_point = ['high', 'vhigh', '3', 'more', 'med', 'med']

def find_best_split(dataset, labels):
    best_gain = 0
    best_feature = 0
    #chooses 3 unique numbers(replace=False) from all nums in dataset
    features = np.random.choice(len(dataset[0]),3,replace=False)
    for feature in features:
        data_subsets, label_subsets = split(dataset, labels, feature)
        gain = information_gain(labels, label_subsets)
        if gain > best_gain:
            best_gain, best_feature = gain, feature
    return best_gain, best_feature

#creating randoming indices
indices = [random.randint(0,999) for x in range(1000)]
#list comp splitting data and labels
data_subset = [car_data[i] for i in indices]
labels_subset = [car_labels[i] for i in indices]

#creating new tree from training data set
subset_tree = build_tree(data_subset, labels_subset)
print_tree(subset_tree)

#returns best info gain and index of best feature to split at
print(find_best_split(data_subset,labels_subset))

#classifying data points using entire forest
#classification of unlabeled point using 20 subset trees
predictions = []
for i in range(20):
    indices = [random.randint(0, 999) for i in range(1000)]
    data_subset = [car_data[index] for index in indices]
    labels_subset = [car_labels[index] for index in indices]
    subset_tree = build_tree(data_subset, labels_subset)

    # classification of unlabeled point using 1 subset tree
    predictions.append(classify(unlabeled_point, subset_tree))
# obtains most common element from list
final_prediction = (max(predictions, key=predictions.count))
print(final_prediction)