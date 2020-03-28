from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

#classify, fit, then predict
classifier = KNeighborsClassifier(5)

#.fit(training points, training labels)
classifier.fit(movie_dataset, labels)


#classifying 3 movies grouped as unrated category
#nums correspond to normalized budget, run time, year release
unrated = [[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]]

#.predict parameters list of points to classify, returns list of predictions
predictions = classifier.predict(unrated)

#prints [1 1 0]
print(predictions)