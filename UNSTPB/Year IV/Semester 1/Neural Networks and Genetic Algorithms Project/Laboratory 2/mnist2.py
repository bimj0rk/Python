#%%
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist

# The digits SMALL sklearn dataset - there are just 1797 samples 
(xTrain, tTrain), (xTest, tTest) = mnist.load_data()

n_samples = len(xTrain)

#show the first image of the dataset
plt.imshow(xTrain[0])
plt.title('Digit ' + str(tTrain[0]))

#reshape the data so that we dont have size error with MLPC
xTrain = xTrain.reshape((n_samples, -1))
xTest = xTest.reshape((len(xTest), -1))

#convert to float so that we can normalize the data and have decimal points
xTrain = xTrain.astype('float32')
xTest = xTest.astype('float32')

#normalize the fucking data
xTrain /= 255.
xTest /= 255.

#data = data/data.max() # normalization

# Split the data - don't shouffle -it's already done and we want to compare results
#xTrain, xTest, tTrain, tTest = train_test_split(data, digits.target, test_size = 0.2, shuffle = False) 

#rest of it
mlp = MLPClassifier(hidden_layer_sizes = (20, 20), activation = 'relu', max_iter = 150, alpha = 1e-4, solver = 'sgd', verbose = 1, learning_rate_init = .1)

mlp.fit(xTrain, tTrain)
yTest = mlp.predict(xTest)
print("Training set score: %f" % mlp.score(xTrain, tTrain))
print("Test set score: %f" % mlp.score(xTest, tTest))

print('The accuracy is:',accuracy_score(tTest,yTest)) # accuracy_score(y_true, y_pred)
print('Confusion Matrix is: ') 
print(confusion_matrix(tTest, yTest)) # confusion_matrix(y_true, y_pred) - ON LINES!!!
plt.figure()
plt.plot(mlp.loss_curve_)

# %%
