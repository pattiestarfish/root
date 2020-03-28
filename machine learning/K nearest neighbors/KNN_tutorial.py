star_wars = [125, 1977]
raiders = [115, 1981]
mean_girls = [97, 2004]

# finds distance for any dimensional points
def distance(movie1, movie2):
    distance = 0
    for i in range(len(movie1)):
        distance += (movie1[i] - movie2[i]) ** 2
    distance = distance ** 0.5
    return distance

print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011,
                 1965, 1891, 1978]

# normalizes data
def min_max_normalize(lst):
    normalized = []
    minimum = min(lst)
    maximum = max(lst)
    for val in lst:
        mmn = (val - minimum) / (maximum - minimum)
        normalized.append(mmn)
    return normalized

print(min_max_normalize(release_dates))
# -----------------------------
from movies import training_set, training_labels, validation_set, validation_labels

def distance(movie1, movie2):
    squared_difference = 0
    for i in range(len(movie1)):
        squared_difference += (movie1[i] - movie2[i]) ** 2
    final_distance = squared_difference ** 0.5
    return final_distance

def classify(unknown, dataset, labels, k):
    distances = []
    # Looping through all points in the dataset
    for title in dataset:
        movie = dataset[title]
        distance_to_point = distance(movie, unknown)
        # Adding the distance and point associated with that distance
        distances.append([distance_to_point, title])
    distances.sort()
    # Taking only the k closest points
    neighbors = distances[0:k]
    num_good = 0
    num_bad = 0
    for neighbor in neighbors:
        title = neighbor[1]
        if labels[title] == 0:
            num_bad += 1
        elif labels[title] == 1:
            num_good += 1
    if num_good > num_bad:
        return 1
    else:
        return 0

def find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
    num_correct = 0.0
    for movies in validation_set:
        guess = classify(validation_set[movies], training_set, training_labels, k)
        if (guess == validation_labels[movies]):
            num_correct += 1
        else:
            continue
    # returns validation error
    return num_correct / len(validation_set)

print('Call Me By Your Name' in movie_dataset)
my_movie = [350000, 132, 2017]
normalized_my_movie = normalize_point(my_movie)
print(normalized_my_movie)
print(classify(normalized_my_movie, movie_dataset, movie_labels, 5))

test = (validation_set['Bee Movie'])
print(test)
guess = (classify(test, training_set, training_labels, 5))
print(guess)
if (guess == validation_labels['Bee Movie']):
    print("Correct!")

print(find_validation_accuracy(training_set, training_labels, validation_set, validation_labels, 3))