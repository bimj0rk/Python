'''
3 input XOR
https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier
'''

import numpy as py
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

X = [[0., 0., 0.], [0., 0., 1.], [0., 1., 0.], [0., 1., 1.,], [1., 0., 0.], [1., 0., 1.], [1., 1., 0.], [1., 1., 1.,]]
T = [1, 0, 0, 0, 0, 0, 0, 1]

'''
FLAGS:
    hidden_layer_size: default is 100, in our case we need 8 (I think);
    activation - how does the function transmit the info, search for ReLU and GELU;
    solver - how the weight is recalculated;
    alpha - how fast we are moving on the gradient, recommended value: 1e-5;
    batch_size - not important;
    learning_rate - hand in hand with alpha, if far from solution, it will go faster to solution;
    shuffle - force the function to an ablosute minimum;
    tol - tolerance lmao, recommended value: 1e-5;
    early_stopping - if in less than 10 iterations there is no change, stop;
    n_init smth smth - check docs did not undestand;
    max_fun - again, did not understand.

ATTRIBUTES:
    classes: no of output types,
    loss: portion of false positives/negatives, check confusion matrix,
    loss_curve: not important now, important next year,
    coefs: which weight to which layer (wx),
    intercepts: bias (b),
'''

net = MLPClassifier(hidden_layer_sizes = (4), alpha = 1e-5, tol = 1e-5, solver = 'lbfgs')
net.fit(X, T)

print(net.coefs_)
print(net.intercepts_)

Y = net.predict(X)
print("Acc:", accuracy_score(T, Y))
print(confusion_matrix(T, Y))

#we are cooked.