from sklearn import tree
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import pylab

"""
Features:
    [weight in grams, skin texture]
skin texture:
    0 - bumpy
    1 - smooth
labels:
    0 - apple
    1 - orange
"""

# Learning dataset:
features = [[140, 1], [130, 1], [150, 0], [170, 0], [100, 1], [200, 0], [190, 0], [180, 0], [175, 0], [180, 1]]
labels = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Data to be predicted:
new_fruits = [[165, 0], [145, 0], [170, 1], [110, 1], [90, 0], [210, 1], [220, 0]]

# Classifying algorithm:
classifier = tree.DecisionTreeClassifier(random_state=0)
classifier = classifier.fit(features, labels)
results = classifier.predict(new_fruits)
print(results)

# Plotting:
appleColour = '#B41414'
orangeColour = '#ffc100'
appleGuess = '#e56567'
orangeGuess = '#f0eaab'

figure = plt.figure(figsize=(7, 5))
figureSubplot = figure.add_subplot(1,1,1)

index = 0
for element in features:
    if labels[index] == 0:
        plt.scatter(element[1], element[0], color=appleColour, linewidth=2.0)
    else:
        plt.scatter(element[1], element[0], color=orangeColour, linewidth=2.0)
    index += 1

index = 0
for element in new_fruits:
    if results[index] == 0:
        plt.scatter(element[1], element[0], color=appleGuess, linewidth=2.0)
    else:
        plt.scatter(element[1], element[0], color=orangeGuess, linewidth=2.0)
    index += 1

figureSubplot.set(xticks=[0, 1], xticklabels=["bumpy", "smooth"])
plt.ylabel("Weight in grams", fontsize=11)
plt.xlabel("Skin texture", fontsize=11)
plt.xlim(-0.5, 1.5)

predicted_apple = mpatches.Patch(color=appleGuess, label='predicted apple')
predicted_orange = mpatches.Patch(color=orangeGuess, label='predicted orange')
apple = mpatches.Patch(color=appleColour, label='training apple')
orange = mpatches.Patch(color=orangeColour, label='training orange')
plt.legend(handles=[apple, predicted_apple, orange, predicted_orange])

filename = 'apples-and-oranges.png'
plt.savefig(filename, dpi = 150, bbox_inches='tight')
pylab.show()
plt.close()
