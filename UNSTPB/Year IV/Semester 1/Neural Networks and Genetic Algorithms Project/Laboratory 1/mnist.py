#%%
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier


(xTrain, tTrain), (xTest, yTest) = mnist.load_data()
#rng = np.random.default_rng(seed = None)

net = MLPClassifier(solver = 'lbfgs', alpha = 1e-5, hidden_layer_sizes = (5, 2), random_state = 16)
net.fit(xTrain, tTrain)

n = 5
nInputs = np.size(tTrain)

for l in range(n):
    for c in range(n):
        plt.subplot(n, n, n * l + c + 1)
        randomNo = np.random.randint(nInputs)
        plt.imshow(255 - xTrain[randomNo], cmap = 'gray')
        plt.title(tTrain[randomNo])
# %%