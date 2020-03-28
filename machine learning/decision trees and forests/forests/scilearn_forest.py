def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from cars import training_points, training_labels, testing_points, testing_labels
import warnings
from sklearn.ensemble import RandomForestClassifier

#no added randomness needed since bagging later with randomize for us
classifier = RandomForestClassifier(n_estimators=2000,random_state=0)
forest_model = classifier.fit(training_points, training_labels)
print(forest_model.score(testing_points,testing_labels))