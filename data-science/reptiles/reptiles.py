from sklearn import tree
from matplotlib import pyplot as plt

class Animal(object):

    """
    Features vector:
        [egg-laying, scales, poisonous, cold-blooded, legs]
    """

    def __init__(self, name, features_vector):
        self.name = name
        self.features_vector = features_vector

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features_vector

# Classification:
"""
Labels:
    0 - is not a reptile
    1 - is a reptile
"""

# Learning dataset:
rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
boa = Animal('boa constrictor', [0,1,0,1,0])
dartFrog = Animal('dart frog', [1,0,1,0,4])
alligator = Animal('alligator', [1,1,0,1,4])
cat = Animal('cat', [0, 0, 0, 0, 4])

animals = [rattlesnake, boa, dartFrog, alligator, cat]
labels = [1, 1, 0, 1, 0]

features = []

for animal in animals:
    features.append(animal.getFeatures())

# Animals to be predicted:
chicken = Animal('chicken', [1, 1, 0, 0, 2])
dog = Animal('dog', [0, 0, 0, 0, 4])

predict_animals = [chicken, dog]

features_predict = []

for animal in predict_animals:
    features_predict.append(animal.getFeatures())

# Classifying algorithm:
classifier = tree.DecisionTreeClassifier(random_state=0)
classifier = classifier.fit(features, labels)
results = classifier.predict(features_predict)
print(results)
