from sklearn.datasets import make_blobs
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

X, T = make_blobs(n_samples = 10000, n_features = 10, centers = 10, cluster_std = 4.25, random_state = 17)

plt.subplot(2, 1, 1)
plt.scatter(X[:, 0], X[:, 1], c = T)
plt.title('Blobs')

X_train, X_test, T_train, T_test = train_test_split(X, T, train_size = 0.2, random_state = 17, shuffle = False)

mlp = MLPClassifier(hidden_layer_sizes = (20, 10), activation = 'relu', solver = 'adam', alpha = 1e-5, tol = 1e-4, random_state = 17, verbose = True, max_iter = 2000)

mlp.fit(X_train, T_train)

Y = mlp.predict(X_test)

print('Accuracy score: ', accuracy_score(Y, T_test))
print('Confusion matrix: ')
print(confusion_matrix(Y, T_test))

plt.subplot(2, 1, 2)
plt.plot(mlp.loss_curve_)
plt.title('Loss function')
plt.show()
#does not have overfit