#%%
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X, T = make_blobs(n_samples = 500, n_features = 6, centers = 6, cluster_std = 4, random_state = 1)

plt.close('all')
plt.subplot(2, 1, 1)
plt.scatter(X[:, 0], X[:, 1], c = T)

xTrain, xTest, tTrain, tTest = train_test_split(X, T, shuffle = False, train_size = 0.2)

mlp = MLPClassifier(hidden_layer_sizes = (6), alpha = 1e-5, tol = 1e-5, verbose = True, solver = 'lbfgs', activation = 'relu', random_state = 1)
mlp.fit(xTrain, tTrain)

Y = mlp.predict(xTest)

print(accuracy_score(tTest, Y))
print(confusion_matrix(tTest, Y))
# %%
