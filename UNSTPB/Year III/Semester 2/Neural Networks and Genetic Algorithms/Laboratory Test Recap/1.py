#%%
#no classes: 6
#population: 4500
#standard deviation = 3.5
#make blobs, train test split, classifier, scatter plot, loss/confusion matrix/accuracy

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X, T = make_blobs(n_samples = 450, centers = 6, n_features = 6, cluster_std = 3.5) #n_features = classes, for 6 no of features is enough to be equal to no of classes, for less, classes should be a smaller number

plt.close("all")
plt.subplot(2, 1, 1)
plt.scatter(X[:,0], X[:,1], c = T)

#xTrain, xTest, tTrain, tTest = train_test_split(X, T, shuffle = False, train_size = 0.2)

mlp = MLPClassifier(hidden_layer_sizes = (10), alpha = 1e-5, tol = 1e-5, solver = "lbfgs", verbose = 1, activation = "relu", max_iter = 1500)
mlp.fit(X, T)

Y = mlp.predict(X)

print("Debug - coefficients: ", mlp.coefs_)
print("Debug - intercept: ", mlp.intercepts_)

print("Accuracy score: ", accuracy_score(T, Y))
print("Confusion matrix: ")
print(confusion_matrix(T, Y))

#overfitting cand avem un jump de un ordin intre iteratii in ultimele iteratii  in |proj g|
# %%
