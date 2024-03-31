import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, T = make_blobs(n_samples = 200, centers = 2, n_features = 2, random_state = 0, cluster_std = 2.5)

plt.close("all")
plt.figure(figsize = [5, 8])
plt.subplot(2, 1, 1)
plt.scatter(X[:,0], X[:, 1], c = T)

plt.subplot(2, 1, 2)

net = MLPClassifier(hidden_layer_sizes = (),max_iter = 1500, alpha = 1e-5, solver = "lbfgs", tol = 1e-5, activation = "logistic", random_state = 0, verbose = True)
net.fit(X, T)

Y = net.predict(X)

print("Confusion Matrix: ", confusion_matrix(T, Y))
print("Accuracy: ", accuracy_score(T, Y))

plt.scatter(X[:, 0], X[:, 1], c = Y)