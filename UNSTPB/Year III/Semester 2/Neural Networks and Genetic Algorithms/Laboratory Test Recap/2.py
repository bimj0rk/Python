#%%
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

X, T = make_blobs(n_samples = 300, centers = 4, n_features = 4, cluster_std = 2.5)

plt.close('all')
plt.scatter(X[:, 0], X[:, 1], c =T)

mlp = MLPClassifier(hidden_layer_sizes = (10), activation = 'relu', solver = 'lbfgs', alpha = 1e-5, tol = 1e-5, verbose = True, max_iter = 1000)
xTrain, xTest, tTrain, tTest = train_test_split(X, T, shuffle = False)

mlp.fit(xTrain, tTrain)
Y = mlp.predict(xTest)

print("Accuracy: ", accuracy_score(tTest, Y))
print("Confusion matrix:")
print(confusion_matrix(tTest, Y))
# %%
