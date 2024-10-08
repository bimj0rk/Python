import numpy as np
from keras import layers, utils
from keras.datasets import mnist

numClassses = 10
inputShape = (28, 28, 1)

(xTrain, tTrain), (xTest, tTest) = mnist.load_data()

xTrain = xTrain.astype('float32') / 255
xTest = xTest.astype('float32') / 255

xTrain = np.expand_dims(xTrain, -1)
xTest = np.expand_dims(xTest, -1)

tTrain = utils.to_categorical(tTrain, numClassses)
tTest = utils.to_categorical(tTest, numClassses)

model = keras.Sequential #to-do